---
name: jimeng-storyboard
description: Write production-ready JiMeng 2.0 / Seedance AI video prompts and preproduction packages from scripts, outlines, episode drafts, shot lists, storyboards, or reference images. Use when Codex must request and map assets, lock scene geography and screen direction, create high-quality 3D Chinese-animation shots, assign explicit @image/@video roles, split clips to 15 seconds or less, preserve character and spatial continuity, separate daily cold-realistic scenes from Shanhai warm-gold ink art direction, direct observable micro-performance, anticipate generation failures, validate a storyboard, or deliver a standalone HTML shot document.
---

# Write JiMeng Video Prompts

Turn narrative material into compact, copy-ready JiMeng 2.0 prompts. Optimize for stable 3D characters, explicit reference roles, filmable motion and clean editorial continuity.

## Required references

Read the first four files before drafting. Read the fifth when delivering HTML:

- `references/preproduction-workflow.md` for the asset, space and shot-design gates.
- `references/style-system.md` for the locked 3D daily/Shanhai visual system.
- `references/production-controls.md` for reference roles, camera encoding, render controls and continuity handoffs.
- `references/output-contract.md` for timing, shot fields and delivery format.
- `references/html-delivery.md` when the user requests a production document or final package.

## Repository defaults

- Use 16:9, 24 fps and high-quality semi-realistic 3D Chinese animation unless the user overrides them.
- Treat every supplied image as `R-DESIGN` by default: use it only for face shape, hairstyle, costume, props, palette or spatial design. Do not copy its 2D style, layout or original camera composition.
- Do not treat an image as a first frame, identity lock or style lock unless the user explicitly assigns that role.
- Keep daily reality and Shanhai-order aesthetics in separate generated clips. Characters remain the same 3D models in both worlds.
- Use readable Chinese only in post-production overlays. Keep generated screens and signs abstract.

## Workflow

1. Read the complete requested episode or scene.
2. Produce a scene fact sheet: runtime, world mode, location, characters, props, dialogue, action beats, emotional turns, reveals and continuity facts.
3. Run Gate A — asset lock. Classify each needed asset as supplied, needs generation, text-anchor sufficient or conflict pending. Do not silently invent a production-critical face, costume, prop or location.
4. Assign every upload exactly one primary role from `references/production-controls.md`. Keep a stable master numbering map.
5. Run Gate B — spatial lock for any scene with blocking, eyelines, pursuit, entrances, exits or repeated coverage. Define scene ID, axis ID, zones, character positions, facing, gaze, prop positions and permitted screen direction. Generate a 16:9 overhead map with `scripts/render_spatial_map.py` when useful.
6. If Gate A or Gate B contains a material conflict, stop at the relevant request/lock sheet unless the user authorizes assumptions or asks for a draft. Mark authorized assumptions as provisional.
7. Mark every beat as `D` (daily reality), `S` (Shanhai order) or `T` (explicit in-shot transition).
8. Run Gate C — shot design. Split on changes in action, speaker, camera objective, reveal, emotional turn or world style. Prefer 3–10 seconds; never exceed 15 seconds.
9. Give every shot one primary action, one dominant camera move, one observable micro-performance beat and one visible end state.
10. Encode the starting camera with Z/Y/X/F shorthand. Bind the shot to the approved scene/axis IDs and carry screen direction forward.
11. Select the minimum current-shot asset set. Reference only visible assets that control a property in this shot; do not paste the entire project asset list into every prompt.
12. For an opening, place a visible question, anomaly, threat or emotional wound inside the first two seconds without inventing new plot.
13. Preserve the requested runtime. Carry each shot's end state into the next shot's entry state.
14. Write each visual prompt as `reference-role clause + applicable style prefix + spatially locked shot core + micro-performance + compact risk prevention`.
15. Put dialogue, voice-over, sound and exact interface text outside the visual prompt.
16. Run `scripts/validate_storyboard.py --strict-production --strict-preproduction` for a locked final. Use only `--strict-production` for backward-compatible drafts.
17. When a final production package is requested, generate one standalone source-of-truth HTML file with `scripts/build_storyboard_html.py`. Regenerate it after revisions instead of maintaining contradictory chat versions.

## Reference rules

- State what each `@图片N`, `@视频N` or `@音频N` controls. Never write a bare reference with no purpose.
- When an image is `R-DESIGN`, include: `仅参考设计，不作为首帧，不复刻二维画风与原构图，重新构建为统一3D国漫角色/场景`.
- Use the same character reference number across adjacent shots. Do not silently renumber assets.
- Keep the total uploaded files at 12 or fewer and assign each upload a role.
- Keep the per-shot reference set minimal. Every asset named in `素材映射` must appear in that shot's visual prompt, and every @ reference in the prompt must be declared in `素材映射`.
- If supplied references contradict the script, follow the user's latest explicit direction; otherwise flag the conflict and follow the script.

## Camera and motion rules

- Start from framing, camera height, view angle and focal length; then describe subject action, environmental motion, dominant camera move, lighting and end state.
- Keep one dominant move: locked-off, push, pull, pan, track, orbit, crane or handheld follow.
- Do not combine push and pull, slow and fast, or conflicting screen directions in one clip.
- Avoid large orbit moves at Z1–Z3 close range because they increase face drift. Use Z4 or wider, or reduce the orbit.
- Describe visible behavior instead of abstract emotion. Replace `她很难过` with `笑容停住，视线下移，手指慢慢合上蛋糕盒`.
- For hands, phones, food or vehicles, describe grip, contact, weight and the final pose explicitly.
- Never cross the locked 180-degree axis without a visible neutral-axis shot, motivated camera crossing or a new axis declaration.

## Performance rules

- Translate emotion into visible evidence: gaze target and break, eyelid tension, mouth or jaw change, breath rhythm, hand pressure, shoulder state, posture and weight transfer.
- Use two layers when background characters are visible: foreground subject performance and restrained background response.
- Select two to four decisive cues. Do not stack every facial and body cue into every shot.
- Keep performance filmable. Avoid labels such as “很悲伤” without an observable action.

## Failure pre-mortem

Before finalizing each shot, name the most likely model failures and counter them with positive physical instructions first. Typical risks are identity drift, axis reversal, eyeline mismatch, teleporting props, hand/contact errors, accidental style transfer, unwanted text, background characters stealing focus and camera-motion conflict.

## 3D quality rules

- Keep subjects visibly animated 3D, not live-action and not flat illustration.
- Specify only relevant physical details: Chinese facial anatomy, stable facial rig, PBR skin with restrained subsurface scattering, strand hair, fabric weave, weathered hard surfaces, global illumination and physically plausible rain/fog.
- Use water-ink and danqing as Shanhai environment art direction only: palette, volumetric ink mist, surface microtexture, negative space and warm-gold light. Never flatten characters into paper cutouts or 2D paintings.
- Prefer two or three decisive material/light details over a long render-keyword list.
- Keep negative constraints compact and risk-specific. Positive physical instructions carry more weight.

## Delivery requirements

Return in this order:

1. `制作摘要`
2. `场次事实表`
3. `资产请求与状态`
4. `空间锁定`
5. `素材角色映射`
6. `统一画风前缀`
7. `角色与道具锚点`
8. `分镜提示词`
9. `后期叠字与声音`
10. `校验结果`

Use the exact shot format in `references/output-contract.md`.

If the user requests only one simple insert, the spatial gate may be marked `不适用`. Otherwise return its asset status, spatial/axis lock, asset mapping, camera code, micro-performance, model-risk prevention, complete prompt, dialogue/audio, overlays and validation result without producing a full episode breakdown.
