#!/usr/bin/env python3
"""Validate timing, prompt budgets, asset roles, continuity and camera plans."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SHOT_RE = re.compile(
    r"^#{1,6}\s*镜头\s*(?P<id>\d+)｜"
    r"(?P<start>\d{1,3}:\d{2})[—-](?P<end>\d{1,3}:\d{2})｜"
    r"(?P<duration>\d+(?:\.\d+)?)秒(?:｜(?P<style>[DST]))?\s*$"
)

FIELD_LABELS = (
    "素材映射",
    "参考资产",
    "镜头编码",
    "场景锁定",
    "衔接状态",
    "微表演",
    "模型风险",
    "画面提示词",
    "台词/旁白",
    "声音",
    "后期叠字",
)

REFERENCE_RE = re.compile(r"@(?:图片|视频|音频)\d+")
ROLE_RE = re.compile(r"R-(?:DESIGN|IDENTITY|FIRST|SCENE|MOTION|AUDIO|STYLE)")
OBSERVABLE_PERFORMANCE_RE = re.compile(
    r"目线|视线|眼睑|眨眼|眉|嘴角|下颌|吞咽|呼吸|吸气|屏息|吐气|"
    r"指尖|抓握|手指|肩|颈|姿态|重心|前脚|后脚|停步|转身"
)

MOVE_PATTERNS = {
    "locked": re.compile(r"固定|锁定机位|locked[- ]?off", re.I),
    "push": re.compile(r"推近|推进|dolly\s*in|push\s*in", re.I),
    "pull": re.compile(r"拉远|后拉|dolly\s*out|pull\s*out", re.I),
    "pan": re.compile(r"横摇|摇镜|\bpan\b", re.I),
    "track": re.compile(r"跟拍|跟随|追踪|\btrack(?:ing)?\b", re.I),
    "orbit": re.compile(r"环绕|绕拍|\borbit\b", re.I),
    "crane": re.compile(r"升降|吊臂|crane|jib", re.I),
    "handheld": re.compile(r"手持跟拍|handheld", re.I),
}


@dataclass
class Shot:
    line_no: int
    shot_id: str
    start: int
    end: int
    duration: float
    style: str | None
    fields: dict[str, str]


def to_seconds(value: str) -> int:
    minutes, seconds = value.split(":", 1)
    return int(minutes) * 60 + int(seconds)


def extract_fields(block: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    collected: list[str] = []

    def flush() -> None:
        nonlocal current, collected
        if current is not None:
            fields[current] = "\n".join(collected).strip()
        current = None
        collected = []

    for raw_line in block:
        stripped = raw_line.strip()
        matched_label = None
        matched_value = ""
        for label in FIELD_LABELS:
            for separator in ("：", ":"):
                prefix = f"{label}{separator}"
                if stripped.startswith(prefix):
                    matched_label = label
                    matched_value = stripped[len(prefix) :].strip()
                    break
            if matched_label:
                break

        if matched_label:
            flush()
            current = matched_label
            if matched_value:
                collected.append(matched_value)
        elif current is not None:
            collected.append(raw_line.rstrip())

    flush()
    return fields


def extract_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    collected: list[str] = []

    def flush() -> None:
        nonlocal current, collected
        if current is not None:
            sections[current] = "\n".join(collected).strip()
        current = None
        collected = []

    for raw_line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", raw_line.strip())
        if match:
            flush()
            name = match.group(1).strip()
            if not name.startswith("镜头"):
                current = name
            continue
        if current is not None:
            collected.append(raw_line.rstrip())

    flush()
    return sections


def parse_shots(text: str) -> list[Shot]:
    lines = text.splitlines()
    headings: list[tuple[int, re.Match[str]]] = []
    for index, line in enumerate(lines):
        match = SHOT_RE.match(line.strip())
        if match:
            headings.append((index, match))

    shots: list[Shot] = []
    for position, (index, match) in enumerate(headings):
        next_index = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
        fields = extract_fields(lines[index + 1 : next_index])
        shots.append(
            Shot(
                line_no=index + 1,
                shot_id=match.group("id"),
                start=to_seconds(match.group("start")),
                end=to_seconds(match.group("end")),
                duration=float(match.group("duration")),
                style=match.group("style"),
                fields=fields,
            )
        )
    return shots


def camera_move_categories(camera_line: str) -> set[str]:
    movement = camera_line
    marker = re.search(r"运动\s*[：:]\s*(.+)$", camera_line)
    if marker:
        movement = marker.group(1)
    return {name for name, pattern in MOVE_PATTERNS.items() if pattern.search(movement)}


def validate(args: argparse.Namespace) -> tuple[list[str], list[str], dict[str, float]]:
    text = args.storyboard.read_text(encoding="utf-8")
    shots = parse_shots(text)
    sections = extract_sections(text)
    errors: list[str] = []
    warnings: list[str] = []
    prompt_lengths: list[int] = []
    camera_conflicts = 0
    asset_reference_mismatches = 0
    space_lock_missing = 0
    micro_performance_missing = 0
    model_risk_missing = 0

    if not shots:
        errors.append("未找到符合格式的镜头标题。")

    if args.strict_preproduction:
        for required_section in ("场次事实表", "资产请求与状态", "空间锁定"):
            if required_section not in sections:
                errors.append(f"缺少前期制作章节“{required_section}”。")
        spatial_section = sections.get("空间锁定", "")
        if spatial_section and not re.search(
            r"状态\s*[：:=]\s*(?:已确认|草案)|不适用", spatial_section
        ):
            errors.append("“空间锁定”章节必须标明状态：已确认、状态：草案或不适用。")

    for shot in shots:
        prefix = f"镜头{shot.shot_id}（第{shot.line_no}行）"
        if shot.duration <= 0:
            errors.append(f"{prefix}时长必须大于0。")
        if shot.duration > args.max_shot:
            errors.append(f"{prefix}为{shot.duration:g}秒，超过{args.max_shot:g}秒。")
        if abs((shot.end - shot.start) - shot.duration) > 0.01:
            errors.append(
                f"{prefix}时间码跨度{shot.end-shot.start}秒，与标注{shot.duration:g}秒不一致。"
            )

        prompt = shot.fields.get("画面提示词", "").strip()
        if prompt:
            prompt_length = len(prompt)
            prompt_lengths.append(prompt_length)
            if prompt_length > args.max_prompt_chars:
                errors.append(
                    f"{prefix}画面提示词{prompt_length}字符，超过{args.max_prompt_chars}字符。"
                )
            elif prompt_length > args.target_prompt_chars:
                warnings.append(
                    f"{prefix}画面提示词{prompt_length}字符，超过建议值{args.target_prompt_chars}；可删重复画质词。"
                )
        elif args.strict_production:
            errors.append(f"{prefix}缺少画面提示词。")

        if not args.strict_production:
            if not args.strict_preproduction:
                continue

        asset_map = shot.fields.get("素材映射", "")
        if args.strict_production and not asset_map:
            errors.append(f"{prefix}缺少“素材映射”。")
        elif args.strict_production and asset_map.strip() != "无":
            references = set(REFERENCE_RE.findall(asset_map))
            if not REFERENCE_RE.search(asset_map):
                errors.append(f"{prefix}素材映射未使用即梦@图片/@视频/@音频编号。")
            if not ROLE_RE.search(asset_map):
                errors.append(f"{prefix}素材映射缺少R-DESIGN等角色编码。")
            prompt_refs = set(REFERENCE_RE.findall(prompt))
            if references and not prompt_refs:
                errors.append(f"{prefix}画面提示词没有引用素材映射中的@素材。")

        camera_line = shot.fields.get("镜头编码", "")
        if args.strict_production and not camera_line:
            errors.append(f"{prefix}缺少“镜头编码”。")
        elif args.strict_production:
            for axis in ("Z", "Y", "X", "F"):
                if not re.search(rf"\b{axis}\s*\w+", camera_line, re.I):
                    errors.append(f"{prefix}镜头编码缺少{axis}参数。")
            categories = camera_move_categories(camera_line)
            special_zoom = re.search(r"希区柯克|dolly\s*zoom|vertigo", camera_line, re.I)
            if len(categories) > 1 and not special_zoom:
                camera_conflicts += 1
                errors.append(
                    f"{prefix}包含多个主运镜：{', '.join(sorted(categories))}。"
                )
            z_match = re.search(r"\bZ\s*([1-9])\b", camera_line, re.I)
            if z_match and int(z_match.group(1)) <= 3 and "orbit" in categories:
                camera_conflicts += 1
                errors.append(f"{prefix}为Z1-Z3近距离环绕，存在崩脸风险。")

        continuity = shot.fields.get("衔接状态", "")
        if args.strict_production and not continuity:
            errors.append(f"{prefix}缺少“衔接状态”。")
        elif args.strict_production and (
            not re.search(r"入\s*=", continuity) or not re.search(r"出\s*=", continuity)
        ):
            errors.append(f"{prefix}衔接状态必须同时包含“入=”和“出=”。")

        if args.strict_production and prompt and not re.search(r"3D|三维", prompt, re.I):
            errors.append(f"{prefix}未明确要求3D/三维画面。")

        if args.strict_production and "R-DESIGN" in asset_map and prompt:
            if not re.search(r"不作(?:为)?首帧|不作为首帧", prompt):
                errors.append(f"{prefix}R-DESIGN提示词未声明“不作为首帧”。")
            if not re.search(r"不复刻|不复制|不继承", prompt):
                errors.append(f"{prefix}R-DESIGN提示词未声明不复制参考画风/构图。")

        if not args.strict_preproduction:
            continue

        declared_refs = set(REFERENCE_RE.findall(asset_map))
        prompt_refs = set(REFERENCE_RE.findall(prompt))
        undeclared_refs = prompt_refs - declared_refs
        unused_refs = declared_refs - prompt_refs
        if undeclared_refs or unused_refs:
            asset_reference_mismatches += 1
            details: list[str] = []
            if undeclared_refs:
                details.append(f"提示词未声明={','.join(sorted(undeclared_refs))}")
            if unused_refs:
                details.append(f"映射未使用={','.join(sorted(unused_refs))}")
            errors.append(f"{prefix}当前镜头资产集合不一致：{'；'.join(details)}。")
        if len(declared_refs) > args.max_shot_assets:
            warnings.append(
                f"{prefix}使用{len(declared_refs)}个当前镜头参考，超过建议上限"
                f"{args.max_shot_assets}；应拆镜或移除弱参考。"
            )

        spatial_lock = shot.fields.get("场景锁定", "").strip()
        if not spatial_lock:
            space_lock_missing += 1
            errors.append(f"{prefix}缺少“场景锁定”。")
        elif spatial_lock != "不适用":
            if not re.search(r"\bSC\d+\b", spatial_lock, re.I):
                errors.append(f"{prefix}场景锁定缺少SC场次ID。")
            if not re.search(r"\bAX-[A-Z0-9]+\b", spatial_lock, re.I):
                errors.append(f"{prefix}场景锁定缺少AX轴线ID。")
            if not re.search(r"状态\s*[：:=]\s*(?:已确认|草案)", spatial_lock):
                errors.append(f"{prefix}场景锁定缺少已确认/草案状态。")
            if not re.search(r"目线\s*=|运动\s*=|朝向\s*=|面向", spatial_lock):
                errors.append(f"{prefix}场景锁定缺少目线、朝向或运动方向。")

        micro_performance = shot.fields.get("微表演", "").strip()
        if not micro_performance:
            micro_performance_missing += 1
            errors.append(f"{prefix}缺少“微表演”。")
        else:
            if not re.search(r"主体\s*=", micro_performance):
                errors.append(f"{prefix}微表演必须包含“主体=”。")
            if not OBSERVABLE_PERFORMANCE_RE.search(micro_performance):
                errors.append(f"{prefix}微表演缺少可观察的目线、呼吸、手部或重心信号。")

        model_risk = shot.fields.get("模型风险", "").strip()
        if not model_risk:
            model_risk_missing += 1
            errors.append(f"{prefix}缺少“模型风险”。")
        elif not re.search(r"风险\s*=", model_risk) or not re.search(r"预防\s*=", model_risk):
            errors.append(f"{prefix}模型风险必须同时包含“风险=”和“预防=”。")

    for previous, current in zip(shots, shots[1:]):
        if current.start != previous.end:
            relation = "重叠" if current.start < previous.end else "空档"
            errors.append(
                f"镜头{previous.shot_id}到镜头{current.shot_id}存在时间线{relation}："
                f"{previous.end}秒 -> {current.start}秒。"
            )

    total = sum(shot.duration for shot in shots)
    timeline_total = shots[-1].end - shots[0].start if shots else 0
    longest = max((shot.duration for shot in shots), default=0)
    longest_prompt = max(prompt_lengths, default=0)

    if args.expected_total is not None and abs(total - args.expected_total) > 0.01:
        errors.append(f"镜头时长合计{total:g}秒，与期望{args.expected_total:g}秒不一致。")
    if shots and abs(total - timeline_total) > 0.01:
        errors.append(f"镜头时长合计{total:g}秒，与时间线跨度{timeline_total:g}秒不一致。")

    stats = {
        "shots": len(shots),
        "total": total,
        "timeline_total": timeline_total,
        "longest": longest,
        "longest_prompt": longest_prompt,
        "camera_conflicts": camera_conflicts,
        "asset_reference_mismatches": asset_reference_mismatches,
        "space_lock_missing": space_lock_missing,
        "micro_performance_missing": micro_performance_missing,
        "model_risk_missing": model_risk_missing,
    }
    return errors, warnings, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("storyboard", type=Path)
    parser.add_argument("--expected-total", type=float)
    parser.add_argument("--max-shot", type=float, default=15.0)
    parser.add_argument("--target-prompt-chars", type=int, default=900)
    parser.add_argument("--max-prompt-chars", type=int, default=1900)
    parser.add_argument("--max-shot-assets", type=int, default=4)
    parser.add_argument(
        "--strict-production",
        action="store_true",
        help="Require asset roles, Z/Y/X/F camera code, continuity handoffs and 3D constraints.",
    )
    parser.add_argument(
        "--strict-preproduction",
        action="store_true",
        help="Require preproduction sections, spatial locks, micro-performance, model-risk prevention and exact per-shot asset sets.",
    )
    args = parser.parse_args()

    errors, warnings, stats = validate(args)
    print(
        f"镜头数={int(stats['shots'])} 总时长={stats['total']:g}秒 "
        f"时间线跨度={stats['timeline_total']:g}秒 最长镜头={stats['longest']:g}秒 "
        f"最长提示词={int(stats['longest_prompt'])}字符 运镜冲突={int(stats['camera_conflicts'])} "
        f"资产引用不一致={int(stats['asset_reference_mismatches'])} "
        f"空间锁定缺失={int(stats['space_lock_missing'])} "
        f"微表演缺失={int(stats['micro_performance_missing'])} "
        f"模型风险缺失={int(stats['model_risk_missing'])}"
    )
    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 时长、时间线、提示词预算与已启用的生产/前期锁定规则均通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
