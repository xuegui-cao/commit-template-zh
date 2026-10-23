# Changelog

## 1.2.1+zh.1 (2026-10-23)

- 25 UI strings localized to a bilingual `English (中文)` format
  (dialog title/button, 10 form labels + 2 tooltips, 11 commit-type radio
  captions, commit-panel action text)
- plugin.xml version suffixed to `1.2.1+zh.1`, bilingual description note
- Reproducible build pipeline added: `tools/localize_jar.py` + self-check
  `tools/verify_jar.py` (all bilingual strings asserted against the built JAR)
- Localization reference sources annexed inside the distribution JAR
  (`src/`, `tests/`, `resources/META-INF/plugin.xml`, `LICENSE`, `README.zh-CN.md`)
- Functional behavior unchanged from upstream 1.2.1; template markers
  (`BREAKING CHANGE:`, `Closes`, lowercase type names) intentionally untouched
