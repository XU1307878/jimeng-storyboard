# Default reference shot format

Use this as the default user-facing prompt structure. It mirrors the supplied reference's director-readable layout while preserving the skill's continuity and generation controls.

## Production segment

- One production segment represents approximately 15–30 seconds of edited story time.
- A segment contains several numbered shots, commonly 1.5–8 seconds each.
- Choose shot duration from action and rhythm; do not force equal lengths.
- The sum of internal shot durations must equal the stated segment duration.
- When the target generator has a 15-second limit, group the numbered shots into two or more sealed generation clips of 15 seconds or less. Preserve the same shot numbering and clearly mark the clip boundary.
- Do not stretch one uninterrupted camera move to 30 seconds merely to satisfy the segment duration.

## Opening material line

Only list assets the user actually supplied or explicitly mapped:

```text
女生@图1，场景@图2，色卡@图3，全景@图4，关灯场景@图5
```

Do not create a separate fictional appearance lock. When a character reference exists, use its tag and state only the action-critical feature visible in that shot. When no reference or script description exists, do not invent hair color, eye color, costume condition, facial marks or body type.

Do not inherit the medium or style from an example format. Unless explicitly supplied for the current project, omit `3D`, `真人`, `二维`, `古风`, `虚幻引擎`, named rendering engines, aspect ratio and frame rate. A reference prompt controls structure only unless the user says it also controls visual style.

Then write:

```text
题材与基调 / 气质参照：
<genre, emotional temperature, photographic behavior and pacing; describe observable qualities instead of relying only on named works>
```

## Exact per-shot structure

```text
【第 N 镜 · X 秒】

画面：
<景别与构图。按时间顺序写主体动作、微动作、环境反馈和落幅；需要精确节奏时标注第几秒。>

表演：
动作=<可见身体行为、接触关系与动作结果>；表情=<观众直接读到的主要情绪或社会性伪装>；微表情=<二至四个眼神、眉间、嘴角、下颌、呼吸或手指压力信号>。

机位：
<高度及选择理由> | 类型 = <正面/侧面/3/4/俯拍/仰拍等> | 轴线侧 = <A侧/B侧/中性/无>

镜头：
<焦段> <景别> <唯一主运镜及理由>
起幅：<首帧可见状态> → 落幅：<镜尾可继承状态>

视线：
<脸部角度> | 眼神落点 = <具体人物、道具或空间位置> | 留白侧 = <方向及叙事用途>

光影·大气：
主光 = <来源、方向、软硬、色温>
明暗分区 = <主体和环境的受光/阴影关系>
色板 = <只在有价值时给关键颜色或HEX；颜色绑定材质、光源和叙事作用>
粒子 = <类型 × 密度 × 运动反馈，或“无”>
介质 = <雾、雨、尘、烟、黑暗或“无”>

衔接：
<上镜落幅如何进入本镜起幅；动作、视线、声音、遮挡或构图匹配；首镜写“本段起镜”。>

台词：
<角色名：“原台词。” / 画外音 / —>

声音：
环境声：<空间底噪> | 动作声：<同步反馈> | 音乐：<进入、变化、停止> | 人物声/画外声：<如适用>
```

Use the field names and order exactly unless the user supplies a newer reference format.

## Content rules

### 画面

- Start with shot size and composition: centered, offset, symmetrical, rule of thirds or foreground obstruction.
- Put the character at a measurable position such as camera-left 2/5 or center-right.
- Write the action as a visible sequence with one primary action per shot.
- Include two to four decisive performance cues, not a catalogue of micro-actions.
- State relevant physical feedback: cloth drag, hair lag, foot contact, prop weight, rain, fog or dust.

### 表演三层

- `动作`回答人物实际做了什么，并写明起点、接触和可继承的结束状态。
- `表情`回答观众第一眼读到的主要情绪；悬疑或欺骗场景允许写社会性伪装。
- `微表情`用二至四个可观察信号揭示强度、转折或潜台词，不堆满所有面部和身体细节。
- 当外在表情与真实意图冲突时明确写出对照，例如：`表情=故作关切；微表情=回答前视线短暂避开、下颌瞬间收紧`。
- 背景人物同样遵守三层逻辑，但动作幅度和微表情密度必须低于主体。

### 机位与镜头

- Give a short narrative reason for camera height, framing and movement.
- Keep the camera on the declared axis side; use a neutral shot or visible crossing before changing sides.
- Use one focal length and one dominant move.
- `起幅` is the actual first-frame lock and `落幅` is the actual last-frame lock; a separate lock section is unnecessary.

### 视线

- State face angle and a concrete gaze target.
- State the side of negative space when it guides movement, threat or expectation.
- If the face is outside frame or invisible, write that directly rather than inventing a gaze.

### 光影·大气

- Keep key-light origin and white balance stable within a scene unless a scripted light event changes them.
- Describe a light change with timing and physical cause. Avoid unexplained exposure or color jumps.
- Do not require particles or a color code when the scene does not need them.

### 衔接

- Make the prior shot's last pose, movement, gaze, prop state or sound become the current shot's entry trigger.
- Name hard cut, match cut, insert, reverse, occlusion or continuous movement when useful.
- If a cut changes scale, explain the preserved spatial or action relationship.

### 台词与声音

- Preserve the script's exact dialogue; do not rewrite it for convenience.
- Distinguish dialogue, voice-over and offscreen speech.
- Synchronize action sounds to visible contact.
- Carry a useful ambience, music phrase or sound tail across cuts.

## Hidden continuity pass

Before delivery, check without adding extra visible sections unless a problem must be reported:

- character identity and supplied-reference usage;
- costume and physical state stated by script/reference;
- left/right position, axis and gaze;
- prop hand, contact and end position;
- key-light source, color temperature and exposure changes;
- weather, particles and surface condition;
- dialogue attribution and mouth movement;
- environmental, action and music continuity;
- internal shot total and any 15-second generator boundaries.
