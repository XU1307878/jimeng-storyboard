---
name: haohui-director
description: Analyze Chinese short-drama scripts, select a genre-specific directing treatment, design dramatic shot progression, and hand the approved plan to a model-specific storyboard skill. Use for director readings, opening hooks, genre treatment, shot design, performance direction, or continuity planning; do not treat it as a JiMeng or MiniMax H3 prompt adapter by itself.
---

# Haohui Short-Drama Director

中文名称：**浩辉短剧导演**。用户可以直接说“用浩辉短剧导演研读这个剧本”。内部调用标识仍为 `$haohui-director`。

Use the imported 24-module library as a selective directing reference, not as 24 simultaneous system prompts. Direct the script first; let the explicitly chosen generation platform control final prompt syntax, duration and reference mechanics.

## Required reading

1. Read [references/routing-matrix.md](references/routing-matrix.md) to select one primary mode and, only when helpful, one accent mode.
2. Read [references/director-core.md](references/director-core.md) for the shared dramaturgy, shot, performance and continuity workflow.
3. Read [references/audience-platform-rhythm.md](references/audience-platform-rhythm.md) when the audience orientation, opening retention, episode rhythm or male/female/general-audience treatment affects the directing decision.
4. Read [references/camera-action-physics.md](references/camera-action-physics.md) only for pursuit, combat, forceful action, complex movement or a request to strengthen camera language.
5. Read [references/spatial-blocking-relay.md](references/spatial-blocking-relay.md) for multi-character dialogue, fixed seating, entrances/exits, cross-shot movement or a shot that must reserve space for later action.
6. Read [references/cinematic-storytelling-1-51.md](references/cinematic-storytelling-1-51.md) when converting exposition or emotion into visible action, choosing composition/editing/time/sound grammar, or designing a motivated transition. Use it as a decision library, not a checklist.
7. Read [references/three-system-production-loop.md](references/three-system-production-loop.md) when the user requests a complete AI-film workflow, reusable asset states, production-grade prompt review, result diagnosis, retry planning or iterative shot repair.
8. Read only the selected genre reference:
   - [references/genre-realistic-drama.md](references/genre-realistic-drama.md) for romance, workplace, life, rebirth, revenge, melodrama, family power, science fiction or suspense.
   - [references/genre-animation-spectacle.md](references/genre-animation-spectacle.md) for xianxia combat, poetic ink CG, grounded wuxia, 3D comedy, mythic epic, medieval underworld fantasy or black-gold CG.
9. Read [references/platform-handoff.md](references/platform-handoff.md) only when the user requests production prompts or names a video model.

## Non-negotiable boundaries

- Preserve the script's events, causality, character relationships, dialogue meaning and emotional turns. A genre formula is a candidate treatment, never permission to rewrite the story.
- Do not assume live action, 2D, 3D, aspect ratio, rendering engine, camera package, frame rate, music or clip duration. Use the user's established project choices; otherwise mark material choices as pending.
- Do not generate character or scene assets merely because the workflow locks them. Asset, geography and axis locks are textual production decisions unless the user explicitly requests images or diagrams.
- Keep model families isolated. Never import H3 interface assumptions into JiMeng/Seedance output or JiMeng syntax and duration rules into H3 output.
- Translate title- or filmmaker-based style labels into observable cinematography, production design, rhythm, material and performance attributes. Do not ask a model to copy a named creator's signature style.
- Do not paste fixed genre formulas into every scene. Apply a technique only when it expresses the current beat and remains physically filmable.
- Treat the source pack's module 10 as unreliable: its title says comeback/revenge but its body duplicates romance guidance. Use the reconstructed revenge rules in the genre reference instead.
- Prefer positive, visible directions. Do not simulate prompt weighting by keyword repetition, arbitrary numbers or long generic quality suffixes.

## Working mode

When given a script:

1. Read the complete requested episode or bounded scene.
2. Identify the dramatic question, audience knowledge, conflict, reversal, emotional turn, hook opportunity and ending obligation.
3. Classify the audience orientation and narrative engine from evidence, not from the protagonist's gender. Record primary audience, secondary audience, identification route, payoff mechanism and confidence when the distinction affects treatment.
4. Select the primary genre mode from the routing matrix. Add one accent mode only when it solves a distinct secondary need.
5. Establish or inherit a platform rhythm profile when the work is retention-driven. State the first 3-second, 15-second and 30-second tasks without forcing every story into the same speed.
6. Lock characters, locations, critical props, time of day, motivated light sources, scene geography, screen direction and eyelines in text. For blocking-sensitive scenes, confirm whether reference-image placement is binding; also identify allowed visible cast, delayed entrants and offscreen voices. Make the smallest script-consistent assumption for missing details and label it provisional.
7. Design shots by information gain and emotional causality, not by a fixed five-shot ladder. Every retained shot must change action, emotion, information, spatial understanding or sound.
8. Before selecting a conspicuous convention, state its dramatic job in one phrase. Choose the least elaborate spatial, compositional, editing, temporal or sound device that makes that job visible; omit the device if dialogue and performance already carry the beat.
9. Give each visible performance three compatible layers: action, readable expression and two to four decisive micro-expression cues. Tie the change to a visible or audible trigger.
10. For forceful action, design the visible chain `起势 → 接触点/作用点 → 受力结果 → 反应/恢复 → 镜尾状态`; choose camera behavior only after the action geometry is clear.
11. Carry the outgoing body pose, gaze, prop contact, light state and sound cue into the next shot's entry state. For movement, preserve `start → route → interaction point → endpoint`, and reserve enough frame space for the next meaningful action without revealing delayed entrants early.
12. If the user requested a model-specific prompt, hand the director plan to the correct adapter under the rules in `platform-handoff.md`. Otherwise stop at an editable director treatment or storyboard plan.
13. Run a final check for plot fidelity, axis, eyeline, identity, props, lighting, sound, action physics, timing and medium consistency.
14. When revising a generated failure, preserve every verified successful layer, classify the visible failure, change one main variable and define one observable acceptance point. Split an overloaded shot instead of rewriting unrelated successful controls.

## Delivery

Match the user's requested scope. If they ask for only the opening or first shot, do not dump the whole production bible. For a full director treatment, use:

1. `导演研读`
2. `题材路由与选择理由`
3. `受众方向与平台节奏`（仅在影响创作时）
4. `场次事实表`
5. `文字资产锁定`
6. `空间与轴线锁定`
7. `剧情分镜与节奏`
8. `连续性风险`
9. `平台交接说明`

Default to editable Markdown or TXT. Produce DOCX only when requested. Do not render images, HTML or other assets unless explicitly requested.
