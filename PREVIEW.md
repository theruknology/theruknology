# Preview and maintenance

Open `README.md` in VS Code and press **Ctrl+Shift+V** (macOS: **Cmd+Shift+V**). Relative SVG images resolve locally. The Peek GIF requires internet access.

For a wider browser preview, open `preview.html` directly in your browser. It includes a light/dark toggle and needs no install or build server. This approximates GitHub's README layout; GitHub controls the final spacing, sanitization, and image rendering. Check a narrow browser window too. Projects use a two-column grid; earlier-stage work is in an expandable section.

The illustrated header uses a slowly rotating rosette with reduced-motion support. The header is a self-contained SVG and remains visible without animation. The Peek GIF shows the actual project.

Edit `README.md` directly, then run `python3 scripts/build-profile.py` to refresh the browser preview and artwork. No dependencies required. Commit the `assets/` directory with the README. Nothing has been committed or pushed automatically.

## Content research

Reviewed the public repository listing and these project READMEs on November 3, 2026:

- https://github.com/theruknology?tab=repositories
- https://github.com/theruknology/govessel
- https://github.com/theruknology/shahmat2
- https://github.com/theruknology/agentprobe
- https://github.com/theruknology/agent-bazaar
- https://github.com/theruknology/llm-rs
- https://github.com/theruknology/peek

This is a curated public-work profile, not an exhaustive audit of every repository or private work. Project descriptions reflect their documentation, not an independent execution audit. No benchmark claims or publication authorship were inferred. Existing social links were preserved from the previous README. The contribution snake is embedded again, with custom coral and blue palettes.

## Editorial references

Reviewed https://github.com/antirez, https://github.com/torvalds, https://github.com/simonw, https://github.com/karpathy and https://github.com/antfu for profile presentation. The revision takes its main cues from the first three: brief introductions, concrete descriptions and visible work. No personal copy or visual assets were copied.

## Contribution animation

The browser preview uses recolored snapshots of the existing published contribution snake, downloaded November 3, 2026. They preserve the original contribution pattern and animation; the snapshot’s underlying data may be older. The theme button switches between light and dark variants. These snapshots are not live stats.

The README points to the live `output` branch. After pushing, the snake workflow runs when its configuration changes, every 12 hours, or via Actions → Refresh Profile → Run workflow. The new colors appear after its first successful run. Until then, VS Code/GitHub may display the previously published colors. No workflow was triggered remotely during this edit.

Palette options follow https://github.com/Platane/snk#usage. The locally recolored snapshots also disable animation for reduced-motion preferences.

## Statistics

The six counters use GitHub's public REST API: stars and forks received on owned non-fork repositories, public repositories (including forks), public authored pull requests and issues (open and closed), and followers. These are current totals, not lifetime counts of deleted content. Private activity and commit totals are not included. A commit search count would not reliably match the contribution graph, so it is not presented as an all-time total.

`python3 scripts/build-stats.py` refreshes the data and both SVGs. `python3 scripts/build-stats.py --offline` redraws them from `data/github-stats.json`. No additional dependencies or personal token are required. The scheduled workflow uses its built-in GitHub token and commits refreshed cards to the default checkout branch, then publishes the snake to `output`. Branch rules must allow the bot to push for automatic stats updates. If an API request fails or search is incomplete, the fetch aborts before replacing existing cards. The checked-in cards work immediately after pushing, even before the first scheduled refresh.
