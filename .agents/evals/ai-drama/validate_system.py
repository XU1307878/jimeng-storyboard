from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILLS = ROOT / ".agents" / "skills"
CASES = Path(__file__).with_name("cases.json")

REQUIRED_SKILLS = {
    "haohui-dialogue-doctor",
    "haohui-director",
    "haohui-production-bible",
    "haohui-production-orchestrator",
    "haohui-script-doctor",
    "haohui-sound-director",
    "haohui-video-review",
    "jimeng-storyboard",
    "minimax-h3-storyboard",
}

MIRROR_DIRS = ("agents", "references", "scripts")
H3_FORBIDDEN = (
    "待补充",
    "Seedance 2.0 二次元打戏提示词系统",
    "WorkBuddy",
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def frontmatter_name(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*[\"']?([^\r\n\"']+)", text)
    return match.group(1).strip() if match else None


def check_skill_entries(failures: list[str]) -> None:
    found: set[str] = set()
    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        name = frontmatter_name(skill_file)
        if not name:
            fail(f"missing frontmatter name: {skill_file}", failures)
            continue
        if name in found:
            fail(f"duplicate skill name: {name}", failures)
        found.add(name)
        text = skill_file.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (skill_file.parent / target).resolve()
            if not resolved.exists():
                fail(f"broken reference in {name}: {target}", failures)
    missing = REQUIRED_SKILLS - found
    if missing:
        fail(f"missing discoverable skills: {sorted(missing)}", failures)


def relative_files(base: Path) -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    for name in ("SKILL.md",):
        path = base / name
        if path.exists():
            result[name] = path.read_bytes()
    for directory in MIRROR_DIRS:
        root = base / directory
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                result[path.relative_to(base).as_posix()] = path.read_bytes()
    return result


def check_jimeng_mirror(failures: list[str]) -> None:
    canonical = relative_files(SKILLS / "jimeng-storyboard")
    release = relative_files(ROOT)
    if canonical.keys() != release.keys():
        only_canonical = sorted(canonical.keys() - release.keys())
        only_release = sorted(release.keys() - canonical.keys())
        fail(
            f"jimeng mirror file mismatch: only canonical={only_canonical}, only release={only_release}",
            failures,
        )
        return
    changed = [name for name in canonical if canonical[name] != release[name]]
    if changed:
        fail(f"jimeng mirror content mismatch: {changed}", failures)


def check_h3_isolation(failures: list[str]) -> None:
    h3 = SKILLS / "minimax-h3-storyboard"
    if (h3 / "references" / "legacy-source").exists():
        fail("unverified legacy-source remains inside active H3 skill", failures)
    for path in h3.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in H3_FORBIDDEN:
            if marker in text:
                fail(f"H3 active-source contamination '{marker}' in {path.relative_to(ROOT)}", failures)


def check_eval_cases(failures: list[str]) -> None:
    data = json.loads(CASES.read_text(encoding="utf-8"))
    if len(data) != 8:
        fail(f"expected 8 eval cases, found {len(data)}", failures)
    ids: set[str] = set()
    for case in data:
        required = {"id", "title", "route", "request", "fixture", "expected_invariants", "forbidden"}
        missing = required - case.keys()
        if missing:
            fail(f"eval case missing fields {sorted(missing)}: {case.get('id')}", failures)
            continue
        if case["id"] in ids:
            fail(f"duplicate eval case id: {case['id']}", failures)
        ids.add(case["id"])
        unknown = set(case["route"]) - REQUIRED_SKILLS
        if unknown:
            fail(f"unknown route in {case['id']}: {sorted(unknown)}", failures)
        if len(case["expected_invariants"]) < 4 or not case["forbidden"]:
            fail(f"eval case lacks meaningful assertions: {case['id']}", failures)


def main() -> int:
    failures: list[str] = []
    check_skill_entries(failures)
    check_jimeng_mirror(failures)
    check_h3_isolation(failures)
    check_eval_cases(failures)
    if failures:
        print("FAIL")
        for item in failures:
            print(f"- {item}")
        return 1
    print("PASS: skill discovery, references, JiMeng mirror, H3 isolation, and 8 eval cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
