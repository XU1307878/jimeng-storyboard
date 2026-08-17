# Output contract

## Timing

- Hard maximum: 15 seconds per shot.
- Preferred range: 3–10 seconds.
- Use 1–2 seconds for flashes, inserts, impact cuts or black frames.
- Use 3–6 seconds for close-ups, reactions, phone inserts and one dialogue beat.
- Use 5–10 seconds for travel, reveals, handoffs and controlled camera moves.
- Sum all shot durations and match the requested runtime.
- Keep timestamps continuous with no overlaps or gaps.

## Required response order

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

For a provisional draft, mark the production state in `制作摘要` and each unresolved gate. Do not label it final.

## Preproduction sections

`场次事实表` must identify stable scene IDs and distinguish script facts from assumptions.

`资产请求与状态` must classify each production asset as `已提供`, `需要生成`, `文本锚定`, `冲突待确认` or `不适用`.

`空间锁定` must include `状态：已确认` or `状态：草案`. For blocking-sensitive scenes, include scene ID, axis ID, positions, facing/eyeline, prop positions and permitted screen direction. Use `不适用` only for a genuinely simple insert.

## Asset map format

```markdown
## 素材角色映射

- @图片1（姜禾）：R-DESIGN，只参考脸型、短黑发、青灰骑手服和旧红围巾；不作首帧，不复制二维画风与原构图。
- @图片2（出租屋）：R-SCENE，只参考空间布局、旧家具和冷色照明；机位按本镜重新设计。
```

If there is no uploaded asset, write `无` and rely on the character/scene anchors.

## Shot format

Use this exact format:

```markdown
## 镜头01｜0:00—0:05｜5秒｜D

素材映射：@图片1（姜禾，R-DESIGN）；@图片2（出租屋，R-SCENE）

镜头编码：Z4 / Y4 / X2 / F50mm；运动：缓慢推近

场景锁定：SC01 / AX-A / 状态=已确认；人物=姜禾L1面向右，外婆R2面向左；目线=姜禾→外婆；道具=蛋糕盒在姜禾双手；运动=姜禾左→右

衔接状态：入=姜禾站在桌左侧，双手托住蛋糕盒；出=蛋糕盒落桌，姜禾右手仍搭在盒盖上

本镜新增：姜禾的期待第一次转为迟疑，蛋糕盒成为情绪落点

微表演：主体=姜禾短吸气，视线从外婆移到蛋糕盒，右手指尖压紧盒盖，重心退到后脚；背景=外婆保持不动，只轻微抬眼

模型风险：风险=目线反转、蛋糕盒换手；预防=姜禾始终向画面右侧看，双手持续接触盒体，结尾右手仍在盒盖上

画面提示词：
<reference-role clause, 3D style, visible framing, one action, environment motion, one camera move, light, end state, compact constraints>

台词/旁白：<exact line or “无”>

声音：环境底噪=<room tone>；动作反馈=<synchronized contact sound>；人物声/画外声=<as applicable>；衔接尾巴=<sound carried into the next shot or “无”>

后期叠字：<exact text or “无”>
```

The style letter means:

- `D`: daily 3D cold realism.
- `S`: Shanhai 3D warm-gold ink art direction.
- `T`: an explicit in-shot transformation requested by the user.

## Prompt core checklist

Each `画面提示词` must answer:

1. Which uploaded asset controls which property?
2. What is the framing, camera height, view angle and focal length?
3. Who or what is visible?
4. What single primary action occurs?
5. What moves in the environment?
6. What one camera move occurs?
7. What light, palette and relevant 3D materials apply?
8. What visible state ends the clip?
9. Which approved scene/axis and screen direction does it inherit?
10. Which observable micro-performance carries the emotion?
11. Which likely generation failure is actively prevented?
12. What new action, emotion, information or sound change does this shot add?

The set of @ references in `素材映射` must equal the set used in `画面提示词`. Prefer four or fewer current-shot assets.

## Prompt size

- Target 300–900 Unicode characters per visual prompt.
- Hard maximum 1,900 characters, measured with Python `len()` after trimming leading/trailing whitespace.
- Keep negative constraints short and shot-specific.

## Text and audio

- Put exact dialogue outside the visual prompt.
- Put exact UI, order, signage, title and subtitle text under `后期叠字`.
- In the visual prompt, request blank or abstract interface blocks only.
- Separate ambience, effects and score cues under `声音`.
- For clips with internal time beats, describe one motivated sound progression and preserve any useful tail into the next clip.

## Validation summary

End with:

```markdown
校验结果：共 <N> 镜，总时长 <M> 秒；最长镜头 <X> 秒；最长画面提示词 <Y> 字符；超出15秒镜头 0；超出1900字符提示词 0；运镜冲突 0；资产引用不一致 0；空间锁定缺失 0；微表演缺失 0；模型风险缺失 0；时间线无空档、无重叠。
```

If total runtime is estimated rather than supplied, label it as an estimate.
