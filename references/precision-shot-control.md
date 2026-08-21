# Precision shot control

Use this reference for local-canvas clips that need tighter photography, internal edits or difficult optical behavior. These controls refine the existing asset, style and spatial locks; they do not replace them.

## 1. Sealed generation context

Assume each video generation remembers nothing about earlier clips. Every production prompt must be independently executable:

- include only characters, props and references visible in this clip;
- restate only identity and costume facts supplied by the script, user or reference and visible at the chosen shot size; never invent appearance details;
- state the starting pose, hand contact, gaze, screen position and light direction;
- state the ending pose or prop state needed by the next clip;
- never rely on `同上`, `照前镜`, a scene number or an unexplained script summary.

The production document may use scene IDs for human coordination, but the copy-ready prompt must also contain the actual visible facts.

## 2. First-frame test

Before writing motion, mentally freeze frame zero. It must answer:

1. Who or what is already visible?
2. Where is it in camera-left/center/camera-right and near/mid/far depth?
3. Which direction does the body and gaze face?
4. What is each visible hand touching or carrying?
5. Where does the key light originate and where does the shadow fall?
6. What is already moving at frame one?

Avoid an empty first frame unless emptiness is the deliberate story beat. A moving shot should usually begin with a readable subject or motivated foreground object, not wait for the model to invent an entrance.

## 3. Layered spatial description

For complex compositions, describe:

- **foreground**: occlusion, prop or texture that establishes depth;
- **midground**: the primary action and character blocking;
- **background**: stable architecture, restrained extras, weather and escape routes;
- **operator axis**: which side of the action axis the camera occupies;
- **light path**: source, direction, material it strikes and compositional purpose.

Tie color to matter and light. Prefer `走廊暖光擦过酒红天鹅绒裙边，使女主成为冷灰大厅中的唯一暖色焦点` over a disconnected palette list.

## 4. Optics and FOV anchors

Use one optical system consistently. Existing Z/Y/X/F encoding remains the planning source of truth. FOV is an optional generation-language supplement.

| FOV | Approximate lens | Use |
|---|---:|---|
| 107° | 14–16mm | monumental architecture; high distortion risk |
| 84° | 20–24mm | environment and group blocking |
| 63° | 28–35mm | immersive observation and action |
| 47° | 40–50mm | neutral human perspective |
| 29° | 75–85mm | dialogue isolation and portrait compression |
| 18° | 100–135mm | identity-stable close portrait |
| 12° | 180–200mm | distant detail and compressed space |
| 8° | 300–400mm | surveillance or broadcast-like extreme compression |

Rules:

- Use a table value rather than an arbitrary degree when FOV is needed.
- Keep FOV fixed inside one uninterrupted segment.
- In an internally edited clip, declare the shot size and FOV for every segment.
- At 8° or 107°, repeat the FOV at the start and end of that segment, use one stable location reference, and restate the material/light color relationship.
- Do not write both an incompatible focal length and FOV. When uncertain, keep only the familiar focal length.

## 5. Format modes inside one generated clip

Choose one:

- **continuous take**: one camera setup and one dominant move, no internal cut;
- **ordered cuts**: `CUT 1`, `CUT 2`, `CUT 3` when order matters but exact timing does not;
- **timed cuts**: explicit time ranges and cut types when a beat must land precisely;
- **free b-roll**: only when exact continuity and cut placement are unimportant.

For explicit cuts, state that cuts occur only at the specified points. Across internal cuts preserve the same identity, costume, geometry, screen direction, gaze, prop state, weather, white balance and key-light direction.

Example:

```text
0.0–4.0秒：47°中景，女主位于画面左侧，右手仍握契约纸下缘……
4.0秒 HARD CUT
4.0–8.0秒：18°面部近景，目线仍朝画面右侧，手中契约保持同一高度……
8.0秒 INSERT CUT
8.0–11.0秒：12°手部特写，戒指压住纸角……
内部切点仅发生在4.0秒与8.0秒，各段FOV保持稳定。
```

The default user-facing production segment may run 15–30 seconds and contain several numbered shots. When the selected generator accepts at most 15 seconds, divide that segment into at least two sealed generation clips joined by a motivated visual or sound relay.

## 6. Positive physical locks

Correct likely failures by specifying the desired state first:

- `女主双脚持续着地，重心从后脚移到前脚` before `避免漂浮`;
- `右手五指环绕杯身，杯底始终接触桌面` before `避免手部穿模`;
- `主光始终来自画面左后方，鼻影落向右下` before `避免光影跳变`;
- `背景侍从保持远景虚焦与低幅反应` before `背景不得抢焦`.

Use compact negative constraints only after the physical target is clear. Positive-only phrasing is a useful preference, not an absolute rule: explicit exclusions remain appropriate for unwanted text, style leakage, identity drift or known model failure modes.

## 7. Physics and measurement

Use measurements only when they reduce ambiguity:

- vehicles, crowds and fast travel may benefit from approximate speed;
- fog, dust and visibility may benefit from density or visible depth;
- camera tremor may benefit from a small amplitude;
- giant scale is often clearer relative to nearby humans or architecture.

Do not assign artificial numbers to ordinary acting. `她缓慢抬眼，停半拍` is better than a false speed in km/h. Describe gravity, inertia, contact, wetness, fabric drag and secondary motion where they affect the shot.

## 8. Specialized optical patterns

Use only when the story calls for them:

- **distant observation**: 8°–12° tele view, 20–30% soft foreground occlusion, haze between camera and subject, one anchored vantage point;
- **detail-on-wide**: 84° wide view placed close to a small foreground object, with the environment receding behind it;
- **intimate wide**: 63°–84° close face with readable surroundings and controlled edge distortion;
- **whip transition**: allow roughly 0.8 seconds for motion blur between settled subjects; shorter transitions may read as hard cuts;
- **mixed speed**: separate real-time and slow-motion sections with hard cuts rather than changing speed inside one uninterrupted shot.

## 9. Language and style compatibility

- Default to Chinese prompts for the user's local canvas. Use English only when requested or when the target tool demonstrably performs better with it.
- Keep the project-level `统一画风前缀` for cross-shot consistency, but distribute shot-specific lighting, color, optics, performance and physics next to the action they control.
- Do not name directors, signature works or camera bodies as a substitute for describing the visible result.
- Do not force a single-prompt-only response when the user requests an episode, production sheet or HTML package.
