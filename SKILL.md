---
name: jimeng-storyboard
description: Direct scripts into production-ready JiMeng 2.0 / Seedance storyboard prompts and lightweight text or DOCX production documents. Use when Codex must analyze a script, define assets and scene geography in text, design story shots, split generation clips to 15 seconds or less, lock first and last frames, preserve character, spatial, lighting, prop and sound continuity, assign explicit @image/@video roles, validate prompts, or optionally produce advanced visual assets or HTML when explicitly requested.
---

# Write JiMeng Video Prompts

Turn narrative material into compact, copy-ready JiMeng 2.0 prompts. Optimize for explicit reference roles, filmable motion and clean editorial continuity without inventing a visual medium or style.

## Required references

Read the first six files before drafting. Read the seventh for precision cinematography or multi-cut clips. Read the eighth only when the user explicitly requests HTML:

- `references/preproduction-workflow.md` for the asset, space and shot-design gates.
- `references/style-system.md` only for a style explicitly supplied by the user or established by the project; its 3D daily/Shanhai presets are opt-in, not universal defaults.
- `references/production-controls.md` for reference roles, camera encoding, render controls and continuity handoffs.
- `references/output-contract.md` for timing, shot fields and delivery format.
- `references/narrative-audio-chain.md` for information gain, entry/development/exit beats and sound continuity.
- `references/reference-shot-format.md` for the user's default 15–30 second production-segment layout and exact per-shot fields.
- `references/precision-shot-control.md` when a shot needs FOV control, internal cuts, layered depth, optical effects or local-canvas sealed prompts.
- `references/html-delivery.md` when the user requests a production document or final package.

## Repository defaults

- Do not assume 3D animation, live action, 2D animation, ancient style, Unreal Engine, aspect ratio, frame rate or rendering technology. Use only the medium and style explicitly supplied by the user or already established for that project. If missing and materially needed, mark `画面形式/画幅：待指定` or ask one concise question.
- Treat every supplied image as `R-DESIGN` by default: use it only for face shape, hairstyle, costume, props, palette or spatial design. Do not copy its 2D style, layout or original camera composition.
- Do not treat an image as a first frame, identity lock or style lock unless the user explicitly assigns that role.
- When the user explicitly selects the daily/Shanhai dual-world system, keep those aesthetics in separate generated clips and preserve character identity across worlds.
- Use readable Chinese only in post-production overlays. Keep generated screens and signs abstract.
- Default to lightweight director mode: asset locks and spatial/axis locks are written specifications, not requests to generate images, diagrams or renders.
- Default delivery is one editable UTF-8 Markdown or TXT production document. Produce DOCX when requested. Do not create HTML, reference images, spatial maps or other rendered assets unless the user explicitly asks for them.
- Do not invent or output a separate character-appearance lock by default. Character appearance comes only from the script, explicit user direction or supplied references. If none exists, use the character name and story role without fabricating hair, eye, costume or facial details.
- Default final prompt layout is a 15–30 second production segment containing several short numbered shots in the structure defined by `references/reference-shot-format.md`.

## Workflow

1. Read the complete requested episode or scene.
2. Produce a scene fact sheet: runtime, world mode, location, characters, props, dialogue, action beats, emotional turns, reveals and continuity facts.
3. Run Gate A — textual asset lock. List the characters, costumes, scenes and critical props that must remain stable. Classify supplied references and write concise anchors for missing assets; do not generate the assets unless explicitly requested.
4. Assign every upload exactly one primary role from `references/production-controls.md`. Keep a stable master numbering map.
5. Run Gate B — textual spatial lock for any scene with blocking, eyelines, pursuit, entrances, exits or repeated coverage. Define scene ID, axis ID, zones, character positions, facing, gaze, prop positions and permitted screen direction. Do not draw a spatial map unless explicitly requested.
6. If Gate A or Gate B contains missing information, make the smallest script-consistent assumption and mark it as provisional so prompt work can continue. Stop only when conflicting facts would materially change character identity, plot or staging.
7. Mark every beat as `D` (daily reality), `S` (Shanhai order) or `T` (explicit in-shot transition).
8. Run Gate C — shot design. Organize the story into 15–30 second production segments, then split each segment on changes in action, speaker, camera objective, reveal, emotional turn or world style. Individual internal shots are commonly 1.5–8 seconds. If the target generator accepts no more than 15 seconds, divide the segment into sealed generation clips of 15 seconds or less without changing the requested segment structure.
9. Give every shot one primary action, one dominant camera move, one observable micro-performance beat and one visible end state.
10. Build a narrative relay: state the new information contributed by each shot, then make its exit state or sound cue become the next shot's entry trigger. Remove shots that add no action, emotion, information or sound progression.
11. Encode the starting camera with Z/Y/X/F shorthand. Bind the shot to the approved scene/axis IDs and carry screen direction forward.
12. Treat every generated clip as a sealed document with no model memory. Restate the minimum visible facts sourced from the script or references, plus geometry, prop, light and entry state; never rely on “同上” or “延续上一镜” alone and never invent appearance anchors to fill gaps.
13. Select the minimum current-shot asset set. Reference only visible assets that control a property in this shot; do not paste the entire project asset list into every prompt.
14. For an opening, place a visible question, anomaly, threat or emotional wound inside the first two seconds without inventing new plot.
15. Preserve the requested runtime. Carry each shot's end state into the next shot's entry state.
16. Design a three-layer sound bed for every clip: ambience, action feedback and character/voice/offscreen sound as applicable. Let at least one sound parameter change across the clip; never add random noise merely to fill a field.
17. Write each visual prompt as `reference-role clause + applicable style prefix + spatially locked shot core + micro-performance + compact risk prevention`. Distribute scene-specific lighting, color, optics, performance and physics next to the content they govern instead of repeating generic style prose.
18. Put dialogue, voice-over, sound and exact interface text outside the visual prompt.
19. Run `scripts/validate_storyboard.py --strict-production --strict-preproduction` for a locked final. Use only `--strict-production` for backward-compatible drafts.
20. Save the final production content as a single editable Markdown/TXT source by default, or DOCX when requested. Generate standalone HTML with `scripts/build_storyboard_html.py` only when the user explicitly requests a webpage or HTML package.

## Reference rules

- State what each `@图片N`, `@视频N` or `@音频N` controls. Never write a bare reference with no purpose.
- When an image is `R-DESIGN`, include: `仅参考已指定的设计属性，不作为首帧，不照抄原构图；按本项目已确认的画面形式重新构建`. Add `统一3D国漫` only when the user explicitly chose that medium.
- Use the same character reference number across adjacent shots. Do not silently renumber assets.
- Keep the total uploaded files at 12 or fewer and assign each upload a role.
- Keep the per-shot reference set minimal. Every asset named in `素材映射` must appear in that shot's visual prompt, and every @ reference in the prompt must be declared in `素材映射`.
- If supplied references contradict the script, follow the user's latest explicit direction; otherwise flag the conflict and follow the script.

## Camera and motion rules

- Start from framing, camera height, view angle and focal length; then describe subject action, environmental motion, dominant camera move, lighting and end state.
- Make the first frame non-empty and measurable: visible subject, position, orientation, gaze, contact state, foreground/midground/background and motivated light source.
- Keep one dominant move: locked-off, push, pull, pan, track, orbit, crane or handheld follow.
- Do not combine push and pull, slow and fast, or conflicting screen directions in one clip.
- Avoid large orbit moves at Z1–Z3 close range because they increase face drift. Use Z4 or wider, or reduce the orbit.
- Describe visible behavior instead of abstract emotion. Replace `她很难过` with `笑容停住，视线下移，手指慢慢合上蛋糕盒`.
- For hands, phones, food or vehicles, describe grip, contact, weight and the final pose explicitly.
- Never cross the locked 180-degree axis without a visible neutral-axis shot, motivated camera crossing or a new axis declaration.
- Use focal length as the default local-canvas control. Add a discrete FOV anchor only when the target model benefits from it or the shot uses extreme wide/tele optics; do not give contradictory focal length and FOV values.

## Performance rules

- Translate emotion into visible evidence: gaze target and break, eyelid tension, mouth or jaw change, breath rhythm, hand pressure, shoulder state, posture and weight transfer.
- Use two layers when background characters are visible: foreground subject performance and restrained background response.
- Select two to four decisive cues. Do not stack every facial and body cue into every shot.
- Keep performance filmable. Avoid labels such as “很悲伤” without an observable action.

## Failure pre-mortem

Before finalizing each shot, name the most likely model failures and counter them with positive physical instructions first. Phrase the desired stable state before compact exclusions. Typical risks are identity drift, axis reversal, eyeline mismatch, teleporting props, hand/contact errors, accidental style transfer, unwanted text, background characters stealing focus and camera-motion conflict.

## Medium-specific quality rules

- Apply 3D facial-rig, PBR, strand-hair, Unreal Engine or render-language controls only when 3D has been explicitly selected.
- Apply live-action skin, lens and photographic realism only when live action or photoreal footage has been explicitly selected.
- Apply 2D linework, cel shading or illustration controls only when 2D has been explicitly selected.
- Use water-ink and danqing rules only when that art direction is explicitly selected.
- Prefer two or three decisive material/light details over a long render-keyword list.
- Keep negative constraints compact and risk-specific. Positive physical instructions carry more weight.

## Delivery requirements

Use lightweight director delivery by default. Keep asset and spatial reasoning internal or concise; they are continuity checks, not prominent asset-generation tasks. Do not output a separate `人物锁定` or fabricated appearance bible unless the user explicitly requests it.

Return in this order:

1. `制作摘要`
2. `场次事实表`
3. `素材对应`（仅列用户实际提供或明确编号的素材；没有则省略）
4. `题材与基调 / 气质参照`
5. `15–30秒生产段落`（内部逐镜使用参考格式）
6. `连续性检查`
7. `校验结果`

Use the default shot format in `references/reference-shot-format.md`. Use the legacy expanded engineering card in `references/output-contract.md` only when the user explicitly requests技术生产表、资产编码或严格验证格式.

Keep spatial/axis, first/last-frame and model-risk decisions inside the corresponding `机位`、`镜头`、`衔接` and `画面` fields unless the user asks to see separate engineering locks.

Do not generate images, overhead maps, SVG, HTML previews or other rendered materials as an implied part of this workflow. Those are opt-in deliverables.
