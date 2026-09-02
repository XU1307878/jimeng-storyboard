#!/usr/bin/env python3
"""Render a 16:9 overhead scene-lock SVG from a small JSON specification."""

from __future__ import annotations

import argparse
import html
import json
import math
from pathlib import Path
from typing import Any


CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900
PADDING = 70
HEADER_HEIGHT = 95


def escape(value: Any) -> str:
    return html.escape(str(value), quote=True)


def point(value: Any, field: str) -> tuple[float, float]:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{field}必须是[x, y]。")
    return float(value[0]), float(value[1])


def validate_range(value: float, upper: float, field: str) -> None:
    if value < 0 or value > upper:
        raise ValueError(f"{field}={value:g}超出0—{upper:g}。")


def render(spec: dict[str, Any]) -> str:
    scene_id = str(spec.get("scene_id", "")).strip()
    title = str(spec.get("title", "")).strip()
    status = str(spec.get("status", "草案")).strip()
    if not scene_id or not title:
        raise ValueError("必须提供scene_id和title。")

    design_width = float(spec.get("width", 16))
    design_height = float(spec.get("height", 9))
    if design_width <= 0 or design_height <= 0:
        raise ValueError("width和height必须大于0。")

    plot_x = PADDING
    plot_y = HEADER_HEIGHT + 25
    plot_width = CANVAS_WIDTH - PADDING * 2
    plot_height = CANVAS_HEIGHT - plot_y - PADDING

    def xy(raw: Any, field: str) -> tuple[float, float]:
        x, y = point(raw, field)
        validate_range(x, design_width, f"{field}.x")
        validate_range(y, design_height, f"{field}.y")
        return (
            plot_x + x / design_width * plot_width,
            plot_y + y / design_height * plot_height,
        )

    lines: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_WIDTH}" '
            f'height="{CANVAS_HEIGHT}" viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">'
        ),
        "<defs>",
        '<marker id="arrow-gold" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#e2b86b"/></marker>',
        '<marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" fill="#72b8e7"/></marker>',
        '<filter id="shadow"><feDropShadow dx="0" dy="3" stdDeviation="4" '
        'flood-color="#000" flood-opacity=".35"/></filter>',
        "</defs>",
        f'<rect width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}" fill="#101317"/>',
        f'<text x="{PADDING}" y="48" fill="#f4f0e8" font-size="30" '
        f'font-family="Microsoft YaHei, sans-serif" font-weight="700">'
        f'{escape(scene_id)}｜{escape(title)}</text>',
        f'<text x="{CANVAS_WIDTH-PADDING}" y="48" text-anchor="end" '
        f'fill="#e2b86b" font-size="20" font-family="Microsoft YaHei, sans-serif">'
        f'空间锁定：{escape(status)}</text>',
        f'<rect x="{plot_x}" y="{plot_y}" width="{plot_width}" height="{plot_height}" '
        'rx="12" fill="#181d23" stroke="#66717d" stroke-width="2"/>',
    ]

    for index in range(1, int(design_width)):
        gx = plot_x + index / design_width * plot_width
        lines.append(
            f'<line x1="{gx:.2f}" y1="{plot_y}" x2="{gx:.2f}" '
            f'y2="{plot_y+plot_height}" stroke="#2a323b" stroke-width="1"/>'
        )
    for index in range(1, int(design_height)):
        gy = plot_y + index / design_height * plot_height
        lines.append(
            f'<line x1="{plot_x}" y1="{gy:.2f}" x2="{plot_x+plot_width}" '
            f'y2="{gy:.2f}" stroke="#2a323b" stroke-width="1"/>'
        )

    for index, zone in enumerate(spec.get("zones", []), start=1):
        x = float(zone.get("x", 0))
        y = float(zone.get("y", 0))
        width = float(zone.get("w", 0))
        height = float(zone.get("h", 0))
        if width <= 0 or height <= 0:
            raise ValueError(f"zones[{index}]的w和h必须大于0。")
        x1, y1 = xy([x, y], f"zones[{index}]")
        x2, y2 = xy([x + width, y + height], f"zones[{index}].end")
        fill = escape(zone.get("fill", "#26313b"))
        label = escape(zone.get("label", f"区域{index}"))
        lines.extend(
            [
                f'<rect x="{x1:.2f}" y="{y1:.2f}" width="{x2-x1:.2f}" '
                f'height="{y2-y1:.2f}" rx="10" fill="{fill}" fill-opacity=".68" '
                'stroke="#74818e" stroke-width="1.5"/>',
                f'<text x="{x1+14:.2f}" y="{y1+28:.2f}" fill="#c9d1d9" '
                'font-size="18" font-family="Microsoft YaHei, sans-serif">'
                f'{label}</text>',
            ]
        )

    axis = spec.get("axis")
    if axis:
        ax1, ay1 = xy(axis.get("from"), "axis.from")
        ax2, ay2 = xy(axis.get("to"), "axis.to")
        axis_id = escape(axis.get("id", "AX-A"))
        direction = escape(axis.get("screen_direction", ""))
        lines.extend(
            [
                f'<line x1="{ax1:.2f}" y1="{ay1:.2f}" x2="{ax2:.2f}" '
                f'y2="{ay2:.2f}" stroke="#e2b86b" stroke-width="4" '
                'stroke-dasharray="14 10" marker-end="url(#arrow-gold)"/>',
                f'<text x="{(ax1+ax2)/2:.2f}" y="{(ay1+ay2)/2-14:.2f}" '
                'text-anchor="middle" fill="#f0cc89" font-size="20" '
                'font-family="Microsoft YaHei, sans-serif" font-weight="700">'
                f'{axis_id} {direction}</text>',
            ]
        )

    for index, path in enumerate(spec.get("paths", []), start=1):
        raw_points = path.get("points", [])
        if len(raw_points) < 2:
            raise ValueError(f"paths[{index}]至少需要两个点。")
        scaled = [xy(raw, f"paths[{index}].points") for raw in raw_points]
        encoded = " ".join(f"{x:.2f},{y:.2f}" for x, y in scaled)
        color = escape(path.get("color", "#72b8e7"))
        lines.append(
            f'<polyline points="{encoded}" fill="none" stroke="{color}" '
            'stroke-width="5" stroke-linecap="round" stroke-linejoin="round" '
            'marker-end="url(#arrow-blue)"/>'
        )
        label = escape(path.get("label", f"路径{index}"))
        lx, ly = scaled[0]
        lines.append(
            f'<text x="{lx+12:.2f}" y="{ly-12:.2f}" fill="#9bd2f4" '
            'font-size="18" font-family="Microsoft YaHei, sans-serif">'
            f'{label}</text>'
        )

    for index, obj in enumerate(spec.get("objects", []), start=1):
        ox, oy = xy(obj.get("position"), f"objects[{index}].position")
        object_id = escape(obj.get("id", f"O{index}"))
        kind = str(obj.get("kind", "prop"))
        color = escape(obj.get("color", "#d9dde2"))
        if kind == "character":
            lines.append(
                f'<circle cx="{ox:.2f}" cy="{oy:.2f}" r="23" fill="{color}" '
                'stroke="#fff" stroke-width="3" filter="url(#shadow)"/>'
            )
            facing = math.radians(float(obj.get("facing", 0)))
            fx = ox + math.cos(facing) * 48
            fy = oy + math.sin(facing) * 48
            lines.append(
                f'<line x1="{ox:.2f}" y1="{oy:.2f}" x2="{fx:.2f}" y2="{fy:.2f}" '
                f'stroke="{color}" stroke-width="5" marker-end="url(#arrow-blue)"/>'
            )
        else:
            lines.append(
                f'<rect x="{ox-21:.2f}" y="{oy-21:.2f}" width="42" height="42" '
                f'rx="7" fill="{color}" stroke="#fff" stroke-width="2" '
                'filter="url(#shadow)"/>'
            )
        lines.append(
            f'<text x="{ox:.2f}" y="{oy+48:.2f}" text-anchor="middle" '
            'fill="#f4f0e8" font-size="18" font-family="Microsoft YaHei, sans-serif" '
            f'font-weight="700">{object_id}</text>'
        )

    for index, camera in enumerate(spec.get("cameras", []), start=1):
        cx, cy = xy(camera.get("position"), f"cameras[{index}].position")
        tx, ty = xy(camera.get("target"), f"cameras[{index}].target")
        camera_id = escape(camera.get("id", f"C{index:02d}"))
        lines.extend(
            [
                f'<polygon points="{cx:.2f},{cy-22:.2f} {cx-19:.2f},{cy+18:.2f} '
                f'{cx+19:.2f},{cy+18:.2f}" fill="#ef6f6c" stroke="#fff" '
                'stroke-width="2" filter="url(#shadow)"/>',
                f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{tx:.2f}" y2="{ty:.2f}" '
                'stroke="#ef8e8c" stroke-width="2" stroke-dasharray="8 7"/>',
                f'<text x="{cx+26:.2f}" y="{cy+6:.2f}" fill="#ffb3b1" '
                'font-size="18" font-family="Microsoft YaHei, sans-serif" '
                f'font-weight="700">{camera_id}</text>',
            ]
        )

    notes = spec.get("notes", [])
    if notes:
        note_text = "｜".join(escape(item) for item in notes)
        lines.append(
            f'<text x="{PADDING}" y="{CANVAS_HEIGHT-24}" fill="#9aa6b2" '
            'font-size="17" font-family="Microsoft YaHei, sans-serif">'
            f'{note_text}</text>'
        )

    lines.append("</svg>")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    data = json.loads(args.spec.read_text(encoding="utf-8"))
    output = args.output or args.spec.with_suffix(".svg")
    if output.suffix.lower() != ".svg":
        raise SystemExit("--output必须使用.svg扩展名。")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(data), encoding="utf-8")
    print(f"PASS: 已生成16:9空间锁定图 {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
