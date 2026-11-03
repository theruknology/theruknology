"""Fetch public GitHub totals and render self-contained profile cards."""
import argparse
import json
import os
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from html import escape

ROOT = Path(__file__).resolve().parents[1]
USER = 'theruknology'

def get(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'theruknology-profile'}
    if os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    with urlopen(Request('https://api.github.com/' + path, headers=headers), timeout=30) as response:
        return json.load(response)

def fetch():
    user = get('users/' + USER)
    repos = []
    page = 1
    while True:
        batch = get(f'users/{USER}/repos?type=owner&per_page=100&page={page}')
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    def count(kind):
        result = get('search/issues?' + urlencode({'q': f'author:{USER} type:{kind} is:public', 'per_page': 1}))
        if result.get('incomplete_results'):
            raise RuntimeError('GitHub returned incomplete search results; keeping previous cards.')
        return result['total_count']
    originals = [r for r in repos if not r['fork']]
    return {'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d'),
            'repos': user['public_repos'], 'stars': sum(r['stargazers_count'] for r in originals),
            'forks': sum(r['forks_count'] for r in originals), 'followers': user['followers'],
            'prs': count('pr'), 'issues': count('issue')}

def render(data, theme):
    dark = theme == 'dark'
    bg, fg, muted, line = ('#161b22','#f0eee8','#a3adbb','#303947') if dark else ('#f5f0e6','#272b35','#656b76','#ddd6ca')
    colors = ['#ef765c','#869cf2','#dbac52','#77b79c','#bc9cd9','#ef765c']
    items = [('stars','Stars received','owned, non-fork repos'),('repos','Public repositories','including forks'),('prs','Pull requests','authored · public'),('issues','Issues opened','authored · public'),('forks','Repository forks','of owned, non-fork repos'),('followers','Followers','on GitHub')]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="350" viewBox="0 0 960 350" role="img"><title>GitHub public statistics</title><desc>{escape(", ".join(str(data[k])+" "+label for k,label,_ in items))}. Updated {data["updated"]}.</desc><rect width="960" height="350" rx="16" fill="{bg}"/><g font-family="Arial,Helvetica,sans-serif"><text x="28" y="37" font-size="16" font-weight="700" fill="{fg}">GitHub / public activity</text><text x="932" y="37" text-anchor="end" font-size="13" fill="{muted}">Updated {data["updated"]}</text>']
    for i,(key,label,note) in enumerate(items):
        x,y = 28 + (i%3)*312, 66 + (i//3)*140
        out.append(f'<path d="M{x} {y}h280" stroke="{line}"/><circle cx="{x+5}" cy="{y+25}" r="4" fill="{colors[i]}"/><text x="{x+18}" y="{y+30}" fill="{muted}" font-size="15">{label}</text><text x="{x}" y="{y+82}" fill="{fg}" font-size="43" font-weight="700" letter-spacing="-1">{data[key]:,}</text><text x="{x}" y="{y+109}" fill="{muted}" font-size="12">{note}</text>')
    out.append('</g></svg>')
    return ''.join(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT/'assets')
    args = parser.parse_args()
    cache = ROOT/'data/github-stats.json'
    data = json.loads(cache.read_text()) if args.offline else fetch()
    args.output.mkdir(parents=True, exist_ok=True)
    for theme in ('light','dark'):
        (args.output/f'stats-{theme}.svg').write_text(render(data, theme))
    cache.parent.mkdir(exist_ok=True)
    cache.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data))
