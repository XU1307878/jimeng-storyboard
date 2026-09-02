# Standalone HTML delivery

Use a standalone HTML file only when the user explicitly requests HTML, a webpage or a browsable storyboard. A generic request for a production package defaults to Markdown/TXT or DOCX and does not trigger HTML generation.

## Build

Run:

~~~powershell
python scripts/build_storyboard_html.py storyboard.md --output storyboard.html --version v1.0 --strict-production --strict-preproduction
~~~

The builder uses only the Python standard library and creates one self-contained UTF-8 file with embedded CSS and JavaScript. It does not load remote fonts, scripts or images.

## Required content

The HTML must contain:

- project title, version, status and generation time;
- scene fact sheet, asset status and spatial lock sections;
- a card for every shot with duration, style, camera, space/axis lock, current-shot assets, continuity, micro-performance, model risks, visual prompt, dialogue, sound and overlays;
- style filters and text search;
- print-friendly layout;
- a notice that the latest generated HTML is the production source of truth.

## Revision rule

Edit the Markdown source, validate it, then regenerate the HTML. Do not hand-edit the HTML and do not maintain multiple contradictory “final” chat versions.

## Handoff

Deliver both the Markdown source and HTML file when practical. If only one file can be handed off, prefer HTML for review and preserve the Markdown source in the repository.
