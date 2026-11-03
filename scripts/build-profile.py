from pathlib import Path

root = Path(__file__).resolve().parents[1]
# Self-contained vector artwork: no external fonts, scripts or image services.
header = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260"><title>theruknology</title><desc>Coral lettering, an animated blue rosette, and geometric shapes on warm ivory.</desc><style>.rosette{transform-origin:990px 130px;animation:turn 40s linear infinite}@keyframes turn{to{transform:rotate(360deg)}}@media(prefers-reduced-motion:reduce){.rosette{animation:none}}</style><rect width="1200" height="260" rx="16" fill="#f5f0e6"/><path d="M0 230H1200M60 0V260M780 0V260" stroke="#ddd6ca"/><circle cx="60" cy="230" r="7" fill="#ef6549"/><text x="58" y="142" font-family="Arial,Helvetica,sans-serif" font-size="86" font-weight="800" letter-spacing="-5" fill="#e65d42">theruknology</text><text x="64" y="185" font-family="monospace" font-size="18" fill="#55544e">Mohammed Ruknuddin</text><g class="rosette" fill="none" stroke="#536cdc" stroke-width="2">''']
for angle in range(0,180,12):
    header.append(f'<ellipse cx="990" cy="130" rx="112" ry="35" transform="rotate({angle} 990 130)"/>')
header.append('</g><circle cx="990" cy="130" r="15" fill="#efb83f"/><path d="M1148 26v24m-12-12h24" stroke="#e65d42" stroke-width="3"/></svg>')
(root / 'assets/header.svg').write_text(''.join(header))
body = (root / 'README.md').read_text()
# Preview the recolored snapshot until the workflow publishes the live assets.
body = body.replace('https://raw.githubusercontent.com/theruknology/theruknology/output/github-contribution-grid-snake-dark.svg', 'assets/snake-preview-dark.svg')
body = body.replace('https://raw.githubusercontent.com/theruknology/theruknology/output/github-contribution-grid-snake.svg', 'assets/snake-preview-light.svg')
preview='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>theruknology / README preview</title><style>
*{box-sizing:border-box}body{margin:0;background:#0d1117;color:#e6edf3;font:16px/1.65 system-ui,sans-serif}main{max-width:940px;margin:40px auto;padding:32px;border:1px solid #30363d;border-radius:8px}img{max-width:100%;vertical-align:middle}a{color:#a7ceff;text-decoration:none}a:hover{text-decoration:underline}h2{font-size:24px;border-bottom:1px solid #30363d;padding-bottom:9px;margin-top:32px}table{border-collapse:collapse;width:100%}td{border:1px solid #30363d;padding:16px}td p:last-child{margin-bottom:0}hr{border:0;border-top:1px solid #30363d;margin:32px 0}aside{max-width:940px;margin:20px auto;color:#9199a5;font-size:13px;padding:0 20px}button{background:#21262d;color:inherit;border:1px solid #484f58;border-radius:6px;padding:8px 16px;cursor:pointer}body.light{background:#fff;color:#1f2328}.light main,.light td,.light h2{border-color:#d0d7de}.light a{color:#0969da}@media(max-width:600px){main{padding:16px;margin:12px}td{padding:9px;font-size:13px}}
</style><aside>Local README approximation · GitHub controls its final typography and image rendering. <button onclick="toggleTheme()">Toggle light / dark</button></aside><main>'''+body+'''</main><script>
function toggleTheme(){
 const light = !document.body.classList.contains('light');
 document.body.classList.toggle('light', light);
 document.querySelectorAll('picture source').forEach(s => s.media = s.srcset.includes('-light.svg') === light ? 'all' : 'not all');
}
// Align the image with the preview's initial dark theme.
document.querySelectorAll('picture source').forEach(s => s.media = s.srcset.includes('-dark.svg') ? 'all' : 'not all');
</script></html>'''
(root/'preview.html').write_text(preview)
print('Updated artwork and preview.html from README.md')
