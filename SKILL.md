---
name: jimeng-storyboard
description: Direct scripts into production-ready JiMeng 2.0 / Seedance storyboard prompts and lightweight text or DOCX production documents. Use when Codex must analyze a script, define assets and scene geography in text, design story shots, split generation clips to 15 seconds or less, lock first and last frames, preserve character, spatial, lighting, prop and sound continuity, assign explicit @image/@video roles, validate prompts, or optionally produce advanced visual assets or HTML when explicitly requested.
---

# Write JiMeng Video Prompts

Turn narrative material into compact, copy-ready JiMeng 2.0 prompts. Optimize for explicit reference roles, filmable motion and clean editorial continuity without inventing a visual medium or style.

## Required references

Read the core workflow and control references before drafting. Use the specialized references when their stated condition applies:

- `references/preproduction-workflow.md` for the asset, space and shot-design gates.
- `references/spatial-confirmation-workflow.md` whenever a scene has multiple characters, fixed seating, blocking, entrances/exits, reverse coverage, or a reference image that may control character placement.
- `references/style-system.md` only for a style explicitly supplied by the user or established by the project; its 3D daily/Shanhai presets are opt-in, not universal defaults.
- `references/production-controls.md` for reference roles, camera encoding, render controls and continuity handoffs.
- `references/seedance-generation-logic.md` for Seedance-specific prompt density, semantic priority, storyboard intervention and retry diagnosis. Treat its numeric thresholds as production heuristics rather than guaranteed model limits.
- `references/output-contract.md` for timing, shot fields and delivery format.
- `references/narrative-audio-chain.md` for information gain, entry/development/exit beats and sound continuity.
- `references/reference-shot-format.md` for the user's default 15–30 second production-segment layout and exact per-shot fields.
- `references/precision-shot-control.md` when a shot needs FOV control, internal cuts, layered depth, optical effects or local-canvas sealed prompts.
- `references/director-language-library.md` when designing dramatic shot progression, focus changes, ensemble composition, action spectacle, lighting strategy or visible injury continuity.
- `references/camera-movement-grammar.md` when selecting or writing push, pull, pan, truck, follow, pedestal, tilt, orbit, roll, locked-off, handheld or compound camera movement.
- `references/cinematic-lighting-grammar.md` when selecting top, side, back, Rembrandt, soft, hard or volumetric light; when a scene changes lighting; or when light continuity is a generation risk.
- `references/performance-causality-grammar.md` when translating emotion, subtext, dialogue delivery or an emotional turn into action, expression, micro-expression and voice.
- `references/html-delivery.md` when the user requests a production document or final package.

## Repository defaults

- Keep model families isolated. Material identified by the user as MiniMax H3 belongs to a separate H3 workflow and must not be imported, summarized into, or used to modify JiMeng/Seedance prompt rules, even when an attached archive or its internal files are mislabeled as Seedance. Use H3 material only when the user explicitly requests MiniMax H3 output.
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
5. Run Gate B for blocking-sensitive scenes. If a reference image contains people or fixed seating, first ask whether its placement should be locked. Alternatively, offer a pure-text overhead map and wait for the user to confirm it. Only a confirmed reference lock or confirmed text map may define final positions, facing, axis and camera zone.
6. If Gate A or Gate B contains missing information, make the smallest script-consistent assumption only for a draft and label it `待确认`. Never put unconfirmed left/right positions, seating or axis claims into a final copy-ready prompt. Stop when the uncertainty would materially change staging.
7. Mark every beat as `D` (daily reality), `S` (Shanhai order) or `T` (explicit in-shot transition).
8. Run Gate C — shot design. Organize the story into 15–30 second production segments, then split each segment on changes in action, speaker, camera objective, reveal, emotional turn or world style. Individual internal shots are commonly 1.5–8 seconds. If the target generator accepts no more than 15 seconds, divide the segment into sealed generation clips of 15 seconds or less without changing the requested segment structure.
9. Give every shot one primary action, one dominant camera move, one observable micro-performance beat and one visible end state.
9a. Design camera language from the scene's dramatic task. Use a motivated progression such as environment/context → blocking/action → reaction/emotional decision → decisive detail, but omit any rung that adds no new story information. Never force a generic five-shot ladder onto every scene.
9b. Derive performance from the script in this order: `trigger → character appraisal → immediate objective → tactic/social mask → visible action + expression + micro-expression + voice → residual end state`. Keep appraisal and objective in director reasoning; put only filmable or audible evidence into the generation payload.
9c. When entrance timing or hidden presence matters, declare allowed visible cast, delayed entrants and offscreen-only voices. For moving subjects, encode `start → traversable route → interaction point → endpoint` and reserve enough frame space for the route without relocating confirmed blocking.
10. Build a narrative relay: state the new information contributed by each shot, then make its exit state or sound cue become the next shot's entry trigger. Remove shots that add no action, emotion, information or sound progression.
11. Encode the starting camera with Z/Y/X/F shorthand. Bind the shot to the approved scene/axis IDs and carry screen direction forward.
12. Treat every generated clip as a sealed document with no model memory. Restate the minimum visible facts sourced from the script or references, plus geometry, prop, light and entry state; never rely on “同上” or “延续上一镜” alone and never invent appearance anchors to fill gaps.
13. Select the minimum current-shot asset set. Reference only visible assets that control a property in this shot; do not paste the entire project asset list into every prompt.
14. For an opening, place a visible question, anomaly, threat or emotional wound inside the first two seconds without inventing new plot.
15. Preserve the requested runtime. Carry each shot's end state into the next shot's entry state.
16. Design a three-layer sound bed for every clip: ambience, action feedback and character/voice/offscreen sound as applicable. Let at least one sound parameter change across the clip; never add random noise merely to fill a field.
16a. Design lighting from dramatic purpose and a motivated physical source. Encode `source + position/height + direction + softness + color + subject effect + background relationship`; keep those invariants stable across coverage unless a visible source event or character movement causes the change.
17. Write each visual prompt as `reference-role clause + applicable style prefix + spatially locked shot core + micro-performance + compact risk prevention`. Distribute scene-specific lighting, color, optics, performance and physics next to the content they govern instead of repeating generic style prose.
17a. Optimize the model-execution payload in semantic priority order: `current-shot references and roles → starting camera anchor → subject starting state + visible action path → action-triggered camera behavior → timed beat changes → end state/continuity → essential light/style → risk-specific exclusions`. The starting camera anchor establishes the current shot's coordinate frame; it does not override confirmed blocking or asset identity. Do not simulate weight with repeated keywords or invented numeric syntax.
17b. Keep the copyable visual payload near 500 Chinese characters when the shot remains fully specified, with about 600 as a soft diagnostic ceiling. Production labels, dialogue and audio fields do not count toward this visual-payload budget. If compression would remove identity, action, camera, timing, end state or continuity, split the clip instead of deleting those controls.
18. Put dialogue, voice-over, sound and exact interface text outside the visual prompt.
19. Run `scripts/validate_storyboard.py --strict-production --strict-preproduction` for a locked final. Use only `--strict-production` for backward-compatible drafts.
20. Save the final production content as a single editable Markdown/TXT source by default, or DOCX when requested. Generate standalone HTML with `scripts/build_storyboard_html.py` only when the user explicitly requests a webpage or HTML package.

## Reference rules

- State what each `@图片N`, `@视频N` or `@音频N` controls. Never write a bare reference with no purpose.
- When an image is `R-DESIGN`, include: `仅参考已指定的设计属性，不作为首帧，不照抄原构图；按本项目已确认的画面形式重新构建`. Add `统一3D国漫` only when the user explicitly chose that medium.
- Use the same character reference number across adjacent shots. Do not silently renumber assets.
- Keep the total uploaded files at 12 or fewer and assign each upload a role.
- Keep the per-shot reference set minimal. Every asset named in `素材映射` must appear in that shot's visual prompt, and every @ reference in the prompt must be declared in `素材映射`.
- Translate proprietary or invented lore names into visible generic attributes and behavior. A reference can anchor appearance, composition, motion or style, but cannot by itself teach the model an unseen fictional rule.
- If supplied references contradict the script, follow the user's latest explicit direction; otherwise flag the conflict and follow the script.
- A character-in-scene reference does not automatically lock blocking. Ask the user to choose `参考图锁定`, `文字俯视图锁定` or `不锁定`. Once confirmed, that choice overrides generic directing assumptions.

## Camera and motion rules

- Select camera movement from narrative purpose, not from a desire to make the shot look busy. Encode the move as `starting frame + subject trigger + camera path + speed/easing + maintained spatial relation + ending frame`.
- Start from framing, camera height, view angle and focal length; then describe subject action, environmental motion, dominant camera move, lighting and end state.
- For complex motion, establish the starting camera anchor before the action sentence, then express the confirmed world-space route in that camera's visible coordinate frame. Screen-left/right describes observation only and must not redefine locked character placement.
- Treat prompt order as a prioritization heuristic, not proof that the model executes text strictly from left to right.
- Make the first frame non-empty and measurable: visible subject, position, orientation, gaze, contact state, foreground/midground/background and motivated light source.
- Keep one dominant move: locked-off, push, pull, pan, track, orbit, crane or handheld follow.
- Do not combine push and pull, slow and fast, or conflicting screen directions in one clip.
- Avoid large orbit moves at Z1–Z3 close range because they increase face drift. Use Z4 or wider, or reduce the orbit.
- Describe visible behavior instead of abstract emotion. Replace `她很难过` with `笑容停住，视线下移，手指慢慢合上蛋糕盒`.
- For hands, phones, food or vehicles, describe grip, contact, weight and the final pose explicitly.
- Never cross the locked 180-degree axis without a visible neutral-axis shot, motivated camera crossing or a new axis declaration.
- Derive the background-to-camera depth chain before writing an overhead map. Fixed furniture must not move between character layers. Aspect-ratio changes may crop the confirmed space but must not relocate characters.
- For multi-cut generation clips, specify each internal beat as `time range + shot size/viewpoint + subject + visible action + end cue`. If no opening frame is supplied, deliberately state the opening shot size and standing/blocking baseline so the model does not invent an unwanted wide establishing frame.
- Use focal length as the default local-canvas control. Add a discrete FOV anchor only when the target model benefits from it or the shot uses extreme wide/tele optics; do not give contradictory focal length and FOV values.

## Lighting rules

- Do not equate cinematic lighting with low exposure. Preserve readable story information and choose contrast for the beat.
- Select a lighting pattern only when it serves the scene: top light for pressure/concealment, side light for division/conflict, back light for separation/reveal, Rembrandt light for controlled facial ambiguity, soft light for openness/intimacy, hard light for danger/severity, and volumetric light for spatial depth or a motivated beam.
- Name the physical or environmental source whenever possible: ceiling lamp, window, torch, streetlight, phone, doorway or skylight. If the source is outside frame, state its screen direction.
- Keep key-light side, height, softness, color temperature, face exposure and shadow direction continuous across adjacent shots. A reverse angle does not move the source with the camera.
- Add haze, dust or smoke only when the scene plausibly contains a medium that reveals a light beam. Volumetric light is not a universal quality suffix.
- Counter the likely failure of each setup with a visible target: readable eyes under top light, minimum face fill under back light, stable cheek triangle for Rembrandt light, negative fill or background separation under soft light, stable shadow edge under hard light, and fixed beam direction/density under volumetric light.

## Performance rules

- Encode every visible character performance in three layers: `动作` (body behavior, contact and end state), `表情` (the readable primary emotion or social mask), and `微表情` (two to four decisive cues from gaze, eyelids, brows, mouth, jaw, breath or hand pressure). Keep the three layers mutually consistent unless the script requires a deliberate contrast between outward expression and hidden intent.
- Give every emotional change a trigger grounded in the script. If the trigger is visible, show it before the reaction; if it is offscreen, represent it through a precise sound, eyeline or contact cue. Do not paste explanatory backstory into the visual prompt when doing so could cause an unwanted object or location to appear.
- Treat emotion as a transition, not a static label: `baseline → trigger → processing delay → leak/control attempt → end state`. Use timing only for decisive changes.
- Bind spoken performance to the same intention: breath, volume, speed, pitch contour, pauses and articulation must agree with the body and micro-expression, unless the character is deliberately masking emotion.
- Translate emotion into visible evidence: gaze target and break, eyelid tension, mouth or jaw change, breath rhythm, hand pressure, shoulder state, posture and weight transfer.
- Use two layers when background characters are visible: foreground subject performance and restrained background response.
- Select two to four decisive cues. Do not stack every facial and body cue into every shot.
- Prefer asymmetric, sequential cues over a simultaneous “emotion face”: gaze reacts before the head, breath changes before the line, and the mouth or hand may betray what the social mask tries to hide.
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
