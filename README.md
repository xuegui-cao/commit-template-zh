# Git Commit Template (bilingual EN/zh)

Bilingual (English + Chinese) repack of the IntelliJ plugin
**Git Commit Template** (`commit-template-idea-plugin` v1.2.1).

All UI prompts keep the original English text and append a Chinese
translation in the `English (中文)` format — 25 strings in total.
No functional changes.

- Install: download `commit-template-zh-1.2.1.jar` from
  [Releases](../../releases), then **Settings → Plugins → ⚙️ → Install
  Plugin from Disk**, restart the IDE.
- Rebuild (no IntelliJ SDK needed, Python 3.8+):
  `python tools/localize_jar.py --base tools/upstream/... --out dist/...`
- Detailed docs: [README.zh-CN.md](README.zh-CN.md) (Chinese)
- Upstream (Apache-2.0): https://github.com/MobileTribe/commit-template-idea-plugin
- Modification statement: see [NOTICE](NOTICE) · [CHANGELOG.md](CHANGELOG.md)
