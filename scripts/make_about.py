"""Render the existing biography as accessible, animated terminal text."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINES = [
    ("I'm Ayoub, a cybersecurity student and web & software developer", '#e6edf3'),
    ('based in Paris. I build my technical foundations through hands-on', '#c9d1d9'),
    ('projects, with a long-term interest in Governance, Risk & Compliance.', '#c9d1d9'),
    ('Currently learning: React, Node.js and ethical hacking.', '#7ee787'),
    ('Outside tech: gaming and FC Barcelona.', '#8b949e'),
]


def main():
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="240" viewBox="0 0 860 240" role="img" aria-labelledby="title desc">
<title id="title">About Ayoub</title>
<desc id="desc">Ayoub is a cybersecurity student and web and software developer based in Paris, building technical foundations through projects with a long-term interest in GRC. Currently learning React, Node.js and ethical hacking. Interests: gaming and FC Barcelona.</desc>
<style>text{font-family:Consolas,monospace}.typing{animation:type 20s steps(70,end) infinite backwards}.cursor{animation:blink 1.2s step-end infinite}.signal{stroke-dasharray:25 785;animation:travel 8s linear infinite}@keyframes type{0%{clip-path:inset(0 100% 0 0)}7%,96%{clip-path:inset(0)}100%{clip-path:inset(0 100% 0 0)}}@keyframes blink{0%,100%{opacity:0}50%{opacity:.8}}@keyframes travel{to{stroke-dashoffset:-810}}@media(prefers-reduced-motion:reduce){.typing,.cursor,.signal{animation:none}.cursor,.signal{display:none}}</style>
<rect x=".5" y=".5" width="859" height="239" rx="10" fill="#0d1117" stroke="#30363d"/>
<text x="27" y="31" fill="#7ee787" font-size="12">aybskt@github ~ $ cat about.md</text>
<text x="751" y="30" fill="#8b949e" font-size="10">WHO I AM</text>
<path d="M26 48H834" stroke="#21262d"/>
<path class="signal" d="M26 48H834" fill="none" stroke="#39d353" stroke-opacity=".5"/>
''']
    for i, (line, color) in enumerate(LINES):
        y = 65 + i * 27 + (10 if i > 2 else 0)
        parts.append(f'<svg x="27" y="{y}" width="806" height="24" viewBox="0 0 806 24"><g class="typing" style="animation-delay:{i*.5:.1f}s"><text x="0" y="18" fill="{color}" font-size="14">{escape(line)}</text></g></svg>')
    parts.append('<text x="27" y="221" fill="#7ee787" font-size="12">$</text><rect class="cursor" x="43" y="210" width="7" height="13" fill="#7ee787"/></svg>\n')
    (ROOT / 'assets/about.svg').write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    main()
