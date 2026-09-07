"""Animate recorded CLI output; the transcript remains the source of truth."""
from html import escape
from pathlib import Path
import json
import textwrap

ROOT = Path(__file__).resolve().parents[1]


def main():
    records = json.loads((ROOT / 'data/demo-transcripts.json').read_text(encoding='utf-8'))
    for name, title in [('metadata', 'HIDE A MESSAGE → READ IT BACK'), ('checker', 'ANALYZE → FIX HEADERS → VERIFY')]:
        lines = []
        for record in records[name]:
            lines.append(('$ ' + record['command'], '#7ee787'))
            for line in record['stdout'].splitlines():
                lines.extend((wrapped, '#c9d1d9') for wrapped in textwrap.wrap(line, 94))
            lines.append(('', '#8b949e'))
        height = 103 + len(lines) * 23
        parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="{height}" viewBox="0 0 860 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)} — recorded CLI demo</title>
<desc id="desc">Animated replay of actual output captured from the project's compiled Java source. Java launcher and classpath omitted from displayed commands. See data/demo-transcripts.json for the transcript.</desc>
<style>text{{font-family:Consolas,monospace}}.line{{animation:type 18s steps(94,end) infinite backwards}}.progress{{transform-origin:26px 0;animation:progress 18s linear infinite}}@keyframes type{{0%{{clip-path:inset(0 100% 0 0)}}6%,93%{{clip-path:inset(0)}}100%{{clip-path:inset(0 100% 0 0)}}}}@keyframes progress{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}@media(prefers-reduced-motion:reduce){{.line,.progress{{animation:none}}}}</style>
<rect x=".5" y=".5" width="859" height="{height-1}" rx="10" fill="#0a0f13" stroke="#25392c"/>
<text x="27" y="29" fill="#8b949e" font-size="10" letter-spacing="1">{escape(title)}</text>
<text x="720" y="29" fill="#7ee787" font-size="10">CLI REPLAY</text>
<path d="M26 46H834" stroke="#21262d"/>
''']
        for i, (line, color) in enumerate(lines):
            if line:
                parts.append(f'<svg x="27" y="{60+i*23}" width="806" height="22" viewBox="0 0 806 22"><g class="line" style="animation-delay:{i*.45:.2f}s"><text y="16" fill="{color}" font-size="12">{escape(line)}</text></g></svg>')
        parts.append(f'<rect x="26" y="{height-30}" width="808" height="2" fill="#21262d"/><rect class="progress" x="26" y="{height-30}" width="808" height="2" fill="#39d353"/><text x="27" y="{height-10}" fill="#8b949e" font-size="9">Actual output · Java launcher omitted · source {records[name+"_commit"][:7]}</text></svg>\n')
        (ROOT / f'assets/demo-{name}.svg').write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    main()
