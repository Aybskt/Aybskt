"""Build self-contained project cards for GitHub's README image renderer."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    ('metadata-extractor', '01 / FILE ANALYSIS', 'Metadata Extractor',
     'Inspect image metadata. Explore hidden messages.',
     'Image analysis · Metadata · Steganography',
     '<rect x="35" y="54" width="54" height="59" rx="6"/><path d="M46 69H76M46 80H68M46 91H59"/><circle cx="79" cy="100" r="11"/><path d="M87 108L96 117"/>',
     '<path class="scan" d="M42 64H82"/>'),
    ('python-code-checker', '02 / DEVELOPER TOOLS', 'Python Code Checker',
     'Analyze Python code for typing and comment quality.',
     'Static analysis · Python source · Code quality',
     '<rect x="32" y="54" width="65" height="59" rx="6"/><path d="M32 68H97M43 60H45M51 60H53M49 79L41 87L49 95M78 79L86 87L78 95M68 77L60 97"/>',
     '<path class="scan" d="M39 73H90"/>'),
]


def main():
    for slug, category, title, summary, tags, icon, motion in PROJECTS:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="190" viewBox="0 0 860 190" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)} — Java project</title>
<desc id="desc">{escape(summary)} View the source code on GitHub.</desc>
<style>text{{font-family:Consolas,monospace}}.scan{{animation:scan 4s ease-in-out infinite;stroke:#7ee787}}.trace{{stroke-dasharray:36 780;animation:travel 7s linear infinite}}@keyframes scan{{0%,100%{{opacity:0;transform:translateY(0)}}20%,65%{{opacity:.8}}85%{{opacity:0;transform:translateY(28px)}}}}@keyframes travel{{to{{stroke-dashoffset:-816}}}}@media(prefers-reduced-motion:reduce){{.scan,.trace{{animation:none;display:none}}}}</style>
<rect x=".5" y=".5" width="859" height="189" rx="10" fill="#0d1117" stroke="#30363d"/>
<text x="27" y="29" fill="#8b949e" font-size="10" letter-spacing="1.5">{category}</text>
<rect x="764" y="17" width="68" height="23" rx="11" fill="#13251b" stroke="#23402c"/>
<circle cx="779" cy="28.5" r="3" fill="#7ee787"/>
<text x="790" y="32" fill="#b7d9bf" font-size="10">Java</text>
<g fill="none" stroke="#588b66" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icon}{motion}</g>
<text x="122" y="77" fill="#e6edf3" font-size="25" font-weight="600" style="font-family:Segoe UI,Arial,sans-serif">{title}</text>
<text x="123" y="108" fill="#c9d1d9" font-size="14" style="font-family:Segoe UI,Arial,sans-serif">{summary}</text>
<path d="M26 137H834" stroke="#21262d"/>
<path class="trace" d="M26 137H834" stroke="#39d353" stroke-opacity=".55"/>
<text x="27" y="166" fill="#8b949e" font-size="11">{tags}</text>
<text x="665" y="166" fill="#7ee787" font-size="12">View source <tspan dx="9">↗</tspan></text>
</svg>
'''
        (ROOT / f'assets/{slug}.svg').write_text(svg, encoding='utf-8')


if __name__ == '__main__':
    main()
