"""Generate the profile's animated technology badges, without skill ratings."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="306" viewBox="0 0 860 306" role="img" aria-labelledby="title desc">
<title id="title">Toolbox — languages, environment and current learning</title>
<desc id="desc">Languages: Java, Python, JavaScript, PHP, C, HTML and CSS. Environment: Linux, Bash and Git. Currently learning: React, Node.js and ethical hacking.</desc>
<style>text{font-family:Consolas,monospace}.badge{animation:enter .4s both}.trace{stroke-dasharray:28 788;animation:travel 8s linear infinite}.pulse{animation:pulse 3s ease-in-out infinite}@keyframes enter{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:translateY(0)}}@keyframes travel{to{stroke-dashoffset:-816}}@keyframes pulse{0%,100%{opacity:.35}50%{opacity:1}}@media(prefers-reduced-motion:reduce){.badge,.trace,.pulse{animation:none}.trace{display:none}}</style>
<rect x=".5" y=".5" width="859" height="305" rx="10" fill="#0d1117" stroke="#30363d"/>
<path d="M26 109H834M26 199H834" stroke="#21262d"/>
<path class="trace" d="M26 109H834M26 199H834" fill="none" stroke="#39d353" stroke-opacity=".45"/>
''']
    rows = [
        ('01 / LANGUAGES', 'Code I work with', 31, 48, 110,
         [('Jv', 'Java'), ('Py', 'Python'), ('JS', 'JavaScript'), ('<?', 'PHP'), ('C', 'C'), ('<>', 'HTML'), ('#', 'CSS')]),
        ('02 / ENVIRONMENT', 'Tools behind the work', 137, 151, 150,
         [('~', 'Linux'), ('$_', 'Bash'), ('±', 'Git')]),
        ('03 / LEARNING', 'Building my next skills', 227, 241, 206,
         [('⚛', 'React'), ('JS', 'Node.js'), ('>_', 'Ethical hacking')]),
    ]
    for row, (label, subtitle, title_y, badge_y, width, items) in enumerate(rows):
        parts.append(f'<text x="27" y="{title_y}" fill="#8b949e" font-size="10" letter-spacing="1.2">{label}</text>')
        parts.append(f'<text x="833" y="{title_y}" text-anchor="end" fill="#8b949e" font-size="10">{subtitle}</text>')
        for i, (symbol, name) in enumerate(items):
            x = 27 + i * (width + 7)
            parts.append(f'''<g class="badge" style="animation-delay:{row*.25+i*.07:.2f}s">
<rect x="{x}" y="{badge_y}" width="{width}" height="39" rx="6" fill="#121c16" stroke="#25392c"/>
<text x="{x+12}" y="{badge_y+24}" fill="#7ee787" font-size="12">{escape(symbol)}</text>
<text x="{x+38}" y="{badge_y+24}" fill="#e6edf3" font-size="11">{name}</text>
</g>''')
        if row == 2:
            parts.append('<circle class="pulse" cx="713" cy="261" r="3" fill="#7ee787"/><text x="725" y="265" fill="#8b949e" font-size="10">IN PROGRESS</text>')
    parts.append('</svg>\n')
    (ROOT / 'assets/toolbox.svg').write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    main()
