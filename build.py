#!/usr/bin/env python3
"""
Simple static build script: assembles templates/pages by injecting partials.

Usage:
  python build.py

Outputs HTML files to the repository root (overwrites existing files with same name).
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / 'templates'
PARTIALS = TEMPLATES / 'partials'
PAGES = TEMPLATES / 'pages'

def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def build():
    header = read(PARTIALS / 'header.html')
    footer = read(PARTIALS / 'footer.html')

    written = []
    for src in sorted(PAGES.glob('*.html')):
        content = read(src)
        content = content.replace('{{HEADER}}', header).replace('{{FOOTER}}', footer)
        out = ROOT / src.name
        out.write_text(content, encoding='utf-8')
        written.append(out)

    print('Built pages:')
    for f in written:
        print(' -', f.name)

if __name__ == '__main__':
    build()
