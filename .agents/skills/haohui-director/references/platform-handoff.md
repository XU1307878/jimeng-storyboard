# Platform Handoff

The director layer determines story treatment. The platform adapter determines copy-ready syntax, duration handling, reference notation and model-specific diagnostics.

## MiniMax H3

Activate only when the user explicitly says `MiniMax H3`, `H3`, or invokes `$minimax-h3-storyboard`.

- Hand the approved director plan to `$minimax-h3-storyboard`.
- Do not load JiMeng or Seedance references, syntax, reference roles or duration assumptions.
- Preserve the user's requested clip duration. If the H3 interface limit is unknown, mark it for confirmation rather than presenting a source-module value as official.
- Convert any imported `Seedance 2.0` labels into model-neutral filmable direction before the H3 adapter writes the final prompt.

## JiMeng / Seedance

Activate when the user says JiMeng, 即梦, Seedance or invokes `$jimeng-storyboard`.

- Hand the approved director plan to `$jimeng-storyboard`.
- Keep the user's 15–30 second production segment layout when established, but divide actual generation clips to 15 seconds or less under the JiMeng workflow.
- Use explicit `@图片/@视频/@音频` roles only for assets the user actually supplied or numbered.
- Let the JiMeng skill control payload density, first/last-frame locks and validation.

## Wan 3.0

Activate only when the user explicitly says `Wan 3.0`, `Wan3` or invokes `$wan3-storyboard`.

- Hand the approved director plan to `$wan3-storyboard`.
- Use `@ImageN/@VideoN/@AudioN` only for files the user actually uploaded and numbered in the current production input. Planned or missing assets remain `待上传` and cannot be presented as active locks.
- Keep character, scene, prop, first-frame, motion and audio references as separate responsibilities. A prop containing exact text needs its own reference and an explicit text-preservation risk note.
- Let the Wan adapter determine the current interface syntax and duration handling; do not import JiMeng clip rules or H3 field contracts.

## Other or unspecified platform

- Do not pretend the imported modules define official limits or syntax for Kling, Runway, Veo or another model.
- If the user asks only for directing or storyboards, output the director treatment and stop.
- If production prompts are requested but the target model materially affects format, mark `目标平台：待指定` or ask one concise question.

## Handoff packet

Pass only the information the selected adapter needs:

1. requested runtime and aspect ratio;
2. confirmed medium and visual treatment;
3. scene facts and asset/reference map;
4. geometry, axis, screen direction and eyelines;
5. segment purpose and timed shot beats;
6. action, expression, micro-expression and voice transition;
7. prop contact, light source and sound continuity;
8. first state, end state and likely generation failures.

Do not pass source-library boilerplate, private-configuration notices, generic 8K suffixes, fixed camera brands or unrelated genre formulas.
