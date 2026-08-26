---
name: haohui-director
description: Analyze Chinese short-drama scripts, select a genre-specific directing treatment, design dramatic shot progression, and hand the approved plan to a model-specific storyboard skill. Use for director readings, opening hooks, genre treatment, shot design, performance direction, or continuity planning; do not treat it as a JiMeng or MiniMax H3 prompt adapter by itself.
---

# Haohui Short-Drama Director

Use the imported 24-module library as a selective directing reference, not as 24 simultaneous system prompts. Direct the script first; let the explicitly chosen generation platform control final prompt syntax, duration and reference mechanics.

## Required reading

1. Read [references/routing-matrix.md](references/routing-matrix.md) to select one primary mode and, only when helpful, one accent mode.
2. Read [references/director-core.md](references/director-core.md) for the shared dramaturgy, shot, performance and continuity workflow.
3. Read only the selected genre reference:
   - [references/genre-realistic-drama.md](references/genre-realistic-drama.md) for romance, workplace, life, rebirth, revenge, melodrama, family power, science fiction or suspense.
   - [references/genre-animation-spectacle.md](references/genre-animation-spectacle.md) for xianxia combat, poetic ink CG, grounded wuxia, 3D comedy, mythic epic, medieval underworld fantasy or black-gold CG.
4. Read [references/platform-handoff.md](references/platform-handoff.md) only when the user requests production prompts or names a video model.

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
3. Select the primary genre mode from the routing matrix. Add one accent mode only when it solves a distinct secondary need.
4. Lock characters, locations, critical props, time of day, motivated light sources, scene geography, screen direction and eyelines in text. Make the smallest script-consistent assumption for missing details and label it provisional.
5. Design shots by information gain and emotional causality, not by a fixed five-shot ladder. Every retained shot must change action, emotion, information, spatial understanding or sound.
6. Give each visible performance three compatible layers: action, readable expression and two to four decisive micro-expression cues. Tie the change to a visible or audible trigger.
7. Carry the outgoing body pose, gaze, prop contact, light state and sound cue into the next shot's entry state.
8. If the user requested a model-specific prompt, hand the director plan to the correct adapter under the rules in `platform-handoff.md`. Otherwise stop at an editable director treatment or storyboard plan.
9. Run a final check for plot fidelity, axis, eyeline, identity, props, lighting, sound, action physics, timing and medium consistency.

## Delivery

Match the user's requested scope. If they ask for only the opening or first shot, do not dump the whole production bible. For a full director treatment, use:

1. `导演研读`
2. `题材路由与选择理由`
3. `场次事实表`
4. `文字资产锁定`
5. `空间与轴线锁定`
6. `剧情分镜与节奏`
7. `连续性风险`
8. `平台交接说明`

Default to editable Markdown or TXT. Produce DOCX only when requested. Do not render images, HTML or other assets unless explicitly requested.
