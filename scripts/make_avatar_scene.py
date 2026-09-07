"""Frame the original avatar in an animated SVG without changing its pixels."""
import base64
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = Path(sys.argv[1]).read_bytes()
    if not source.startswith(b'\x89PNG\r\n\x1a\n'):
        raise ValueError('Supply the original PNG avatar.')
    encoded = base64.b64encode(source).decode('ascii')
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="400" viewBox="0 0 860 400" role="img" aria-labelledby="title desc">
<title id="title">Ayoub — cybersecurity student and software developer</title>
<desc id="desc">Based in Paris. Exploring cybersecurity, building software, and working toward GRC consulting. Original Minecraft avatar, preserved unchanged.</desc>
<defs>
 <clipPath id="photo"><rect x="484" y="65" width="310" height="310" rx="6"/></clipPath>
 <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#7ee787" stop-opacity="0"/><stop offset="1" stop-color="#7ee787" stop-opacity=".12"/></linearGradient>
</defs>
<style>
 text{font-family:Consolas,monospace}.line{animation:enter .5s both}.scan{animation:scan 4s linear infinite}.frame{stroke-dasharray:.22 .78;animation:draw 4s linear infinite}.cursor{animation:blink 1.5s step-end infinite}.signal{animation:signal 3s ease-out infinite;transform-box:fill-box;transform-origin:center}.packet{stroke-dasharray:20 440;animation:packet 4s linear infinite}.code{animation:code 7s linear infinite}
 @keyframes enter{from{opacity:0;transform:translateX(-5px)}to{opacity:1;transform:translateX(0)}}
 @keyframes scan{0%{opacity:0;transform:translateY(0)}8%,75%{opacity:1}90%,100%{opacity:0;transform:translateY(340px)}}
 @keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
 @keyframes blink{0%,100%{opacity:0}50%{opacity:.8}}
 @keyframes signal{0%{opacity:.7;transform:scale(.5)}100%{opacity:0;transform:scale(2.5)}}
 @keyframes packet{to{stroke-dashoffset:-460}}
 @keyframes code{0%{opacity:0;transform:translateY(-10px)}15%,70%{opacity:.5}100%{opacity:0;transform:translateY(110px)}}
 @media(prefers-reduced-motion:reduce){.line,.scan,.frame,.cursor,.signal,.packet,.code{animation:none}.scan,.cursor,.signal,.packet,.code{display:none}}
</style>
<rect x=".5" y=".5" width="859" height="399" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="32" y="31" fill="#7ee787" font-size="11" letter-spacing="1">AYBSKT / PERSONAL PROFILE</text>
<text x="702" y="30" fill="#8b949e" font-size="10">PARIS, FRANCE</text>
<path d="M24 48H836" stroke="#21262d"/>
<path class="packet" d="M24 48H836" fill="none" stroke="#7ee787" stroke-width="1.5"/>
<g clip-path="url(#photo)">
 <image x="484" y="65" width="310" height="310" href="data:image/png;base64,AVATAR_DATA"/>
 <g class="scan"><rect x="484" y="40" width="310" height="24" fill="url(#scan)"/><path d="M484 64H794" stroke="#7ee787" stroke-opacity=".75"/></g>
 <g class="code" fill="#7ee787" font-size="9"><text x="493" y="85">01001</text><text x="751" y="145">0xAF</text><text x="493" y="227">10110</text></g>
</g>
<path d="M474 90V55H509M769 55H804V90M804 350V385H769M509 385H474V350" fill="none" stroke="#23402c"/>
<path class="frame" pathLength="1" d="M474 90V55H509M769 55H804V90M804 350V385H769M509 385H474V350" fill="none" stroke="#39d353" stroke-opacity=".35"/>
<text class="line" style="animation-delay:.15s;font-family:Segoe UI,Arial,sans-serif" x="30" y="131" fill="#e6edf3" font-size="56" font-weight="650" letter-spacing="-2">Hi, I'm Ayoub.</text>
<text class="line" style="animation-delay:.35s" x="33" y="169" fill="#7ee787" font-size="13">Cybersecurity student</text>
<text class="line" style="animation-delay:.5s" x="33" y="192" fill="#c9d1d9" font-size="13">Web &amp; software developer</text>
<g font-size="13" fill="#8b949e" style="font-family:Segoe UI,Arial,sans-serif">
 <text class="line" style="animation-delay:.7s" x="33" y="236">Exploring how systems work.</text>
 <text class="line" style="animation-delay:.85s" x="33" y="258">Building the skills to make them safer.</text>
</g>
<path d="M33 284H431" stroke="#21262d"/>
<text class="line" style="animation-delay:1s" x="33" y="313" fill="#8b949e" font-size="10" letter-spacing="1">DIRECTION</text>
<text class="line" style="animation-delay:1.15s" x="33" y="335" fill="#c9d1d9" font-size="12">Governance, Risk &amp; Compliance</text>
<text class="line" style="animation-delay:1.3s" x="33" y="372" fill="#7ee787" font-size="11">$ code · secure · repeat</text>
<rect class="cursor" x="198" y="363" width="6" height="11" fill="#7ee787"/>
<circle cx="415" cy="369" r="3" fill="#7ee787"/>
<circle class="signal" cx="415" cy="369" r="6" fill="none" stroke="#7ee787"/>
</svg>
'''.replace('AVATAR_DATA', encoded)
    (ROOT / 'assets/avatar-scene.svg').write_text(svg, encoding='utf-8')


if __name__ == '__main__':
    main()
