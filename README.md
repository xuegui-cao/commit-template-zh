# Git Commit Template (bilingual EN/zh)

Bilingual (English + Chinese) repack of the IntelliJ plugin
**Git Commit Template** (`commit-template-idea-plugin` v1.2.1).

All UI prompts keep the original English text and append a Chinese
translation in the `English (中文)` format — 25 strings in total.
No functional changes.

## Why this fork exists

The upstream plugin is mature, but it targets developers who already know
Conventional Commits. In practice, **many junior developers are not familiar
with the actual meaning of the commit types** (feat / fix / docs / style /
refactor / perf / test / build / ci / chore / revert) — the long one-line
English captions often get misread, the wrong type gets picked, and commit
messages end up inconsistent.

This fork keeps every English caption and appends a Chinese translation,
so developers who are new to Conventional Commits (or not comfortable with
English) can understand **what each type is for** at a glance and pick the
right one — reducing mistyped commits at the source.

- Install: download `commit-template-zh-1.2.1.jar` from
  [Releases](../../releases), then **Settings → Plugins → ⚙️ → Install
  Plugin from Disk**, restart the IDE.
- Rebuild (no IntelliJ SDK needed, Python 3.8+):
  `python tools/localize_jar.py --base tools/upstream/... --out dist/...`
- Detailed docs: [README.zh-CN.md](README.zh-CN.md) (Chinese)
- Upstream (Apache-2.0): https://github.com/MobileTribe/commit-template-idea-plugin
- Modification statement: see [NOTICE](NOTICE) · [CHANGELOG.md](CHANGELOG.md)
