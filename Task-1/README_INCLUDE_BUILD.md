Include-style build
=================

This repository now uses a simple static build step to assemble pages from reusable partials.

Structure:
- `templates/partials/` — header.html and footer.html
- `templates/pages/` — page templates containing `{{HEADER}}` and `{{FOOTER}}` markers
- `build.py` — Python script that injects partials and writes generated pages to the repo root

Usage:

Run the build script (requires Python 3):

```powershell
python build.py
```

This will overwrite the root HTML files (e.g., `index.html`, `about.html`) with the assembled pages.

If you prefer a Node-based or more advanced static site generator, I can convert this to `npm` + `gulp`/`eleventy`/`mustache` on request.
