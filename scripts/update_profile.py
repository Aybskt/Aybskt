"""Generate the contribution SVG using public GitHub data; no dependencies."""
from datetime import date, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353']


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.tips = {}
        self.target = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'td' and attrs.get('data-date'):
            self.cells[attrs['id']] = {
                'date': attrs['data-date'], 'level': int(attrs['data-level'])}
        if tag == 'tool-tip':
            self.target = attrs.get('for')
            if self.target:
                self.tips[self.target] = ''

    def handle_data(self, data):
        if self.target:
            self.tips[self.target] += data

    def handle_endtag(self, tag):
        if tag == 'tool-tip':
            self.target = None

    def days(self):
        result = []
        for key, cell in self.cells.items():
            match = re.match(r'\s*(No|[\d,]+) contributions?\b', self.tips.get(key, ''))
            if not match or cell['level'] not in range(5):
                raise ValueError('GitHub calendar format changed; keeping existing assets.')
            count = 0 if match[1] == 'No' else int(match[1].replace(',', ''))
            result.append(dict(cell, count=count))
        result.sort(key=lambda day: day['date'])
        if not 350 <= len(result) <= 371:
            raise ValueError('Incomplete GitHub calendar; keeping existing assets.')
        dates = [date.fromisoformat(day['date']) for day in result]
        if any(b - a != timedelta(days=1) for a, b in zip(dates, dates[1:])):
            raise ValueError('Non-contiguous GitHub calendar.')
        return result


def text(x, y, content, color='#8b949e', size=12):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{escape(str(content))}</text>'


def render(days):
    start = date.fromisoformat(days[0]['date'])
    start -= timedelta(days=(start.weekday() + 1) % 7)
    cols = (date.fromisoformat(days[-1]['date']) - start).days // 7 + 1
    step = min(14, 750 / cols)
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="860" height="238" viewBox="0 0 860 238" role="img" aria-labelledby="title desc">',
             '<title id="title">Aybskt — GitHub contributions</title>',
             '<desc id="desc">Public contribution calendar, updated daily.</desc>',
             '<style>text{font-family:Consolas,monospace}.day{animation:reveal .55s both}.stats{animation:reveal .5s 3.3s both}.trace{stroke-dasharray:1;animation:trace 1.5s ease-out both}@keyframes reveal{0%{opacity:0;transform:translateY(-12px)}65%{opacity:1;transform:translateY(2px)}100%{opacity:1;transform:translateY(0)}}@keyframes trace{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}@media(prefers-reduced-motion:reduce){.day,.stats,.trace{animation:none}}</style>',
             '<rect x=".5" y=".5" width="859" height="237" rx="12" fill="#0d1117" stroke="#30363d"/>',
             text(26, 31, 'aybskt@github ~ $ ./contributions.sh', '#39d353', 14),
             '<path class="trace" pathLength="1" d="M24 48H836" stroke="#39d353" stroke-opacity=".35"/>']
    last_month = None
    for day in days:
        dt = date.fromisoformat(day['date'])
        col, row = divmod((dt - start).days, 7)
        x, y = 65 + col * step, 82 + row * 14
        if dt.month != last_month and (last_month is None or dt.day <= 7) and col < cols - 2:
            parts.append(text(round(x, 2), 70, dt.strftime('%b'), size=10))
            last_month = dt.month
        parts.append(f'<rect class="day" x="{x:.2f}" y="{y}" width="{step-3:.2f}" height="11" rx="2" fill="{PALETTE[day["level"]]}" style="animation-delay:{.2+(col+row)*.045:.3f}s"><title>{dt}: {day["count"]} contributions</title></rect>')
    for row, label in [(1, 'Mon'), (3, 'Wed'), (5, 'Fri')]:
        parts.append(text(26, 91 + row * 14, label, size=10))
    total = sum(day['count'] for day in days)
    parts += ['<g class="stats">', text(26, 211, f'{total:,} contributions · past year', '#c9d1d9'), text(602, 211, 'Less', size=10)]
    for i, color in enumerate(PALETTE):
        parts.append(f'<rect x="{638+i*17}" y="201" width="12" height="12" rx="2" fill="{color}"/>')
    parts += [text(732, 211, 'More', size=10), '</g></svg>']
    return '\n'.join(parts) + '\n'


def main():
    request = Request('https://github.com/users/Aybskt/contributions', headers={'User-Agent': 'Aybskt-profile', 'Accept-Language': 'en-US'})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode('utf-8')
    parser = CalendarParser()
    parser.feed(html)
    days = parser.days()
    svg = render(days)
    (ROOT / 'assets').mkdir(exist_ok=True)
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'data/contributions.json').write_text(json.dumps(days, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'assets/contributions.svg').write_text(svg, encoding='utf-8')
    print(f'Generated calendar: {len(days)} days, {sum(d["count"] for d in days)} contributions.')


if __name__ == '__main__':
    main()
