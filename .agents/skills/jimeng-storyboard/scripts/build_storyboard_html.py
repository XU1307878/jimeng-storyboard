#!/usr/bin/env python3
"""Build a standalone searchable production HTML from storyboard Markdown."""

from __future__ import annotations

import argparse
import html
import re
from datetime import datetime
from pathlib import Path

from validate_storyboard import extract_sections, parse_shots, validate


SHOT_FIELD_ORDER = (
    "素材映射",
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


def inline_markup(value: str) -> str:
    escaped = html.escape(value, quote=True)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def render_markdown_block(value: str) -> str:
    lines = value.splitlines()
    parts: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith("|") and line.endswith("|"):
            rows: list[list[str]] = []
            while index < len(lines):
                table_line = lines[index].strip()
                if not (table_line.startswith("|") and table_line.endswith("|")):
                    break
                cells = [cell.strip() for cell in table_line.strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    rows.append(cells)
                index += 1
            if rows:
                header, *body = rows
                parts.append("<div class=\"table-wrap\"><table><thead><tr>")
                parts.extend(f"<th>{inline_markup(cell)}</th>" for cell in header)
                parts.append("</tr></thead><tbody>")
                for row in body:
                    parts.append("<tr>")
                    parts.extend(f"<td>{inline_markup(cell)}</td>" for cell in row)
                    parts.append("</tr>")
                parts.append("</tbody></table></div>")
            continue
        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(lines[index].strip()[2:])
                index += 1
            parts.append("<ul>")
            parts.extend(f"<li>{inline_markup(item)}</li>" for item in items)
            parts.append("</ul>")
            continue
        if line.startswith("> "):
            parts.append(f"<blockquote>{inline_markup(line[2:])}</blockquote>")
        else:
            parts.append(f"<p>{inline_markup(line)}</p>")
        index += 1
    return "".join(parts)


def first_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line.strip())
        if match:
            return re.sub(r"[*_`]", "", match.group(1)).strip()
    return fallback


def render_shot(shot) -> str:
    style = shot.style or "U"
    style_name = {"D": "日常冷写实", "S": "山海暖金", "T": "镜内切换"}.get(
        style, "未标记"
    )
    fields: list[str] = []
    for label in SHOT_FIELD_ORDER:
        value = shot.fields.get(label, "").strip() or "无"
        css_class = "prompt" if label == "画面提示词" else ""
        content = (
            f'<pre class="{css_class}">{html.escape(value)}</pre>'
            if label == "画面提示词"
            else f"<p>{inline_markup(value)}</p>"
        )
        fields.append(
            f'<section class="field"><h4>{html.escape(label)}</h4>{content}</section>'
        )
    return (
        f'<article class="shot-card" data-style="{html.escape(style)}">'
        '<header class="shot-head">'
        f"<div><span class=\"shot-id\">镜头{html.escape(shot.shot_id)}</span>"
        f'<span class="chip style-{html.escape(style)}">{html.escape(style_name)}</span></div>'
        f'<div class="time">{shot.start//60}:{shot.start%60:02d}—'
        f'{shot.end//60}:{shot.end%60:02d}｜{shot.duration:g}秒</div>'
        "</header>"
        + "".join(fields)
        + "</article>"
    )


def build_html(
    source: Path,
    text: str,
    version: str,
    status: str,
    generated_at: str,
) -> str:
    title = first_title(text, source.stem)
    sections = extract_sections(text)
    shots = parse_shots(text)

    preproduction_names = (
        "制作摘要",
        "场次事实表",
        "资产请求与状态",
        "空间锁定",
        "素材角色映射",
        "统一画风前缀",
        "角色与道具锚点",
        "后期叠字与声音",
        "校验结果",
    )
    section_cards = []
    for name in preproduction_names:
        value = sections.get(name)
        if value:
            section_cards.append(
                f'<section class="document-card" id="{html.escape(name)}">'
                f"<h2>{html.escape(name)}</h2>{render_markdown_block(value)}</section>"
            )

    template = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<style>
:root{--bg:#0f1216;--panel:#181d23;--line:#303943;--text:#edf0f3;--muted:#9ca8b4;--gold:#e1b66b;--blue:#78b9e4;--red:#ef7b78}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.65 "Microsoft YaHei","PingFang SC",sans-serif}
.wrap{max-width:1240px;margin:auto;padding:36px 24px 80px}.hero{padding:30px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(135deg,#1b2229,#12161b)}
h1{margin:0 0 14px;font-size:32px}.meta{display:flex;flex-wrap:wrap;gap:10px;color:var(--muted)}.meta span,.chip{border:1px solid var(--line);border-radius:999px;padding:4px 11px}
.truth{margin-top:18px;padding:12px 15px;border-left:4px solid var(--gold);background:#211d17;color:#f0d7aa}
.toolbar{position:sticky;top:0;z-index:5;display:flex;gap:10px;flex-wrap:wrap;padding:14px 0;background:rgba(15,18,22,.94);backdrop-filter:blur(10px)}
button,input{border:1px solid var(--line);border-radius:10px;background:#181d23;color:var(--text);padding:9px 12px}button{cursor:pointer}button.active{border-color:var(--gold);color:var(--gold)}input{min-width:260px;flex:1}
.document-card,.shot-card{margin:18px 0;padding:22px;border:1px solid var(--line);border-radius:16px;background:var(--panel);box-shadow:0 8px 26px rgba(0,0,0,.16)}
h2{margin:0 0 14px;color:var(--gold)}.shot-head{display:flex;justify-content:space-between;align-items:center;gap:16px;border-bottom:1px solid var(--line);padding-bottom:14px}
.shot-id{font-size:23px;font-weight:700;margin-right:10px}.style-D{color:var(--blue)}.style-S{color:var(--gold)}.style-T{color:var(--red)}.time{font-weight:700;color:var(--muted)}
.field{display:grid;grid-template-columns:125px 1fr;gap:16px;padding:13px 0;border-bottom:1px dashed #2b333c}.field:last-child{border:0}.field h4,.field p{margin:0}
pre{white-space:pre-wrap;word-break:break-word;margin:0;font:inherit}.prompt{padding:14px;background:#101419;border:1px solid #28313a;border-radius:10px}
table{width:100%;border-collapse:collapse}.table-wrap{overflow:auto}th,td{padding:9px 11px;border:1px solid var(--line);text-align:left;vertical-align:top}th{background:#20262d;color:var(--gold)}
blockquote{margin:12px 0;padding:10px 14px;border-left:3px solid var(--blue);background:#141a20}.hidden{display:none!important}
@media(max-width:760px){.field{grid-template-columns:1fr}.shot-head{align-items:flex-start;flex-direction:column}.wrap{padding:18px 12px 50px}}
@media print{body{background:#fff;color:#111}.wrap{max-width:none;padding:0}.toolbar{display:none}.hero,.document-card,.shot-card{background:#fff;box-shadow:none;border-color:#bbb;break-inside:avoid}.truth{background:#fff4de}.prompt{background:#f6f6f6}}
</style>
</head>
<body>
<main class="wrap">
<section class="hero">
<h1>{{TITLE}}</h1>
<div class="meta"><span>版本 {{VERSION}}</span><span>状态 {{STATUS}}</span><span>生成 {{GENERATED}}</span><span>{{SHOT_COUNT}}镜｜{{TOTAL}}秒</span></div>
<div class="truth">生产唯一版本：以本页及其对应Markdown源文件为准。修改源文件后必须重新校验并生成本页。</div>
</section>
<nav class="toolbar" aria-label="镜头筛选">
<button class="active" data-filter="ALL">全部</button><button data-filter="D">日常 D</button><button data-filter="S">山海 S</button><button data-filter="T">切换 T</button>
<input id="search" type="search" placeholder="搜索人物、场景、道具、提示词……">
</nav>
{{SECTIONS}}
<section id="shots"><h2>分镜提示词</h2>{{SHOTS}}</section>
</main>
<script>
const buttons=[...document.querySelectorAll("[data-filter]")],cards=[...document.querySelectorAll(".shot-card")],search=document.querySelector("#search");
let active="ALL";
function apply(){const q=search.value.trim().toLowerCase();cards.forEach(card=>{const styleOK=active==="ALL"||card.dataset.style===active;const textOK=!q||card.textContent.toLowerCase().includes(q);card.classList.toggle("hidden",!(styleOK&&textOK));});}
buttons.forEach(button=>button.addEventListener("click",()=>{active=button.dataset.filter;buttons.forEach(item=>item.classList.toggle("active",item===button));apply();}));
search.addEventListener("input",apply);
</script>
</body>
</html>
"""
    total = sum(shot.duration for shot in shots)
    replacements = {
        "{{TITLE}}": html.escape(title),
        "{{VERSION}}": html.escape(version),
        "{{STATUS}}": html.escape(status),
        "{{GENERATED}}": html.escape(generated_at),
        "{{SHOT_COUNT}}": str(len(shots)),
        "{{TOTAL}}": f"{total:g}",
        "{{SECTIONS}}": "".join(section_cards),
        "{{SHOTS}}": "".join(render_shot(shot) for shot in shots),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    return template


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("storyboard", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--version", default="v1.0")
    parser.add_argument("--status")
    parser.add_argument("--strict-production", action="store_true")
    parser.add_argument("--strict-preproduction", action="store_true")
    parser.add_argument("--expected-total", type=float)
    parser.add_argument("--max-shot", type=float, default=15.0)
    parser.add_argument("--target-prompt-chars", type=int, default=900)
    parser.add_argument("--max-prompt-chars", type=int, default=1900)
    parser.add_argument("--max-shot-assets", type=int, default=4)
    args = parser.parse_args()

    if args.strict_production or args.strict_preproduction:
        errors, warnings, _ = validate(args)
        for warning in warnings:
            print(f"WARN: {warning}")
        if errors:
            for error in errors:
                print(f"FAIL: {error}")
            return 1

    text = args.storyboard.read_text(encoding="utf-8")
    output = args.output or args.storyboard.with_suffix(".html")
    status = args.status or (
        "已锁定" if args.strict_production and args.strict_preproduction else "草案"
    )
    generated_at = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        build_html(args.storyboard, text, args.version, status, generated_at),
        encoding="utf-8",
    )
    print(f"PASS: 已生成独立HTML生产单 {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
