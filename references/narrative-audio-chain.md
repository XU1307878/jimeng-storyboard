# Narrative and audio relay

Use this layer after the asset and spatial locks. It prevents a storyboard from becoming a set of attractive but disconnected clips.

## 1. Information gain

Every shot must contribute at least one visible or audible change:

- action progresses;
- emotion changes through observable behavior;
- the audience learns new story information;
- a sound approaches, recedes, stops, changes direction or triggers a reaction.

Write the contribution as `本镜新增：...` during planning. If it merely repeats the previous shot and creates no useful rhythm, merge or remove it. Do not invent plot just to satisfy this rule.

## 2. Entry, development and exit

Design each generated clip as one continuous dramatic unit:

1. **进入点**: inherit the previous clip's pose, contact, gaze, camera direction, light and sound tail.
2. **发展点**: perform one primary action and reveal the shot's new information.
3. **离开点**: end on a visible pose, prop state, gaze target, occlusion or sound cue that the next clip can inherit.

For clips longer than 10 seconds, a small turn may sit between development and exit. It is not a license to add a second unrelated action.

Recommended timing:

- 3–6 seconds: entry 1–2s, development 1–3s, exit 1s.
- 7–10 seconds: entry 2–3s, development 3–5s, exit 1–2s.
- 11–15 seconds: setup 3–4s, development 3–4s, turn 3–4s, exit 2–3s.

Timing is elastic. Cut as soon as the narrative task and handoff are complete.

## 3. Cross-shot relay

For each adjacent pair, verify:

- shot B begins from shot A's exit state rather than resetting the scene;
- a hand-held prop remains in the same hand unless the transfer is shown;
- gaze direction and screen direction remain consistent with the locked axis;
- camera momentum either continues naturally or cuts after a settled frame;
- light source, weather and background population do not jump;
- at least one audio tail, reaction trigger or motivated cut connects the pair.

Useful relays include a hand reaching then making contact, footsteps approaching then a handle moving, a head turn then a reverse shot to the target, or an object passing through foreground to motivate a cut.

## 4. Sound layers

Keep sound outside the visual generation prompt. Under `声音`, use only relevant layers:

- `环境底噪`: stable spatial identity such as wind, room tone, rain or distant traffic.
- `动作反馈`: contact sounds synchronized to the primary action, including cloth, footsteps, metal or props.
- `人物声`: dialogue, breath, swallow, exertion or silence with audible breathing.
- `画外声`: only story-motivated offscreen voices, footsteps, doors, vehicles or devices.

The minimum production bed is environment plus action feedback. Add character or offscreen sound when the scene calls for it. Do not force all four layers into every shot, and do not use unrelated noise.

## 5. Sound progression

At least one sound property should change during a clip: level, distance, direction, rhythm, texture or presence. Examples:

- camera pushes closer and breathing becomes slightly clearer;
- footsteps move from right rear to center and stop at the door;
- rain stays constant while a metal impact briefly dominates;
- dialogue ends, room tone returns and a phone vibration becomes the exit cue.

Carry useful sound tails across cuts. Specify the tail in the current shot and the pickup in the next shot.

## 6. Local-canvas time segment format

When the user wants a single copy-ready local-canvas prompt, keep all sub-beats inside one clip block:

```text
【片段NN｜总时长N秒】
素材：@图片1=人物设计；@图片2=场景结构；...
风格锁定：D日常 / S山海；统一3D国漫；不得继承参考图二维画风
空间与衔接：SCxx / AX-x；入=...；出=...
画面与机位：景别、高度、方位、焦段、唯一主运镜
0–Ns：进入点画面 + 动作 + 声音变化
N–Ns：发展点画面 + 动作 + 声音变化
N–Ns：离开点画面 + 动作 + 声音尾巴
台词/旁白：...
声音：环境底噪=...；动作反馈=...；人物声/画外声=...；衔接尾巴=...
模型风险与约束：...
```

Never combine D and S in one generated clip unless the user explicitly requests a `T` transformation. Never exceed 15 seconds; split at a motivated exit point.

## 7. Deliberate exclusions

- Do not require five to eight micro-actions; retain two to four decisive performance cues to protect motion stability.
- Do not name a camera body unless it changes a requested look. Framing, focal length, light and movement are more actionable.
- Do not cap an episode at five shots. Shot count follows runtime and dramatic beats.
- Do not demand constant sound change in every layer. One motivated progression is enough.
