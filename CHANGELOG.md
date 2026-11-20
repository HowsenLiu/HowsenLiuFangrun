# Changelog

All notable changes to HowsenLiu Fangrun are documented here.

## [2.000] — 2026-11-20

### Added

- **Variable font** `HowsenLiuFangrun-VF.ttf` — weight 100–700 (default 400),
  width 75–105, optical size 12–72.
- **Static companions** for software without variable-axis support:
  four static TTFs (Light / Regular / Medium / Bold) and a TTC collection
  for older WPS / legacy systems.
- **Web builds**: full-charset WOFF2, GB2312 subset (8,470 glyphs) and a
  page demo subset (752 glyphs, 0.61 MB).
- Eight specimen plates under `specimen/`.

### Design

- Every corner and terminal gets one circular fillet of 70/1000 em.
- Weight axis comes from native Noto Sans SC variable instances, so stems
  keep their true drawings at every weight.
- Coverage: 33,225 code points / 33,128 glyphs.

### Changed

- Metadata rewritten for the variable build: `fvar`, `STAT`, OS/2,
  name table IDs 0–17, `HVAR` for advance widths.
- Version bumped to 2.000; family name `HowsenLiu Fangrun`,
  subfamily `Variable`.
- Heavy deliverables ship as GitHub Release assets (above the 100 MB
  per-file limit).
- License updated: free for personal and commercial use; modification,
  derivative fonts and redistribution are restricted — see [LICENSE](LICENSE).

### Known limitations

- No TrueType hinting.
- No Latin kerning (`kern` / GPOS pairs).
- Simplified/Traditional regional variants not separated (no `locl`).
- Width axis is a proportional horizontal scale; stems get proportionally
  lighter at 75.

## [1.000] — 2026-11-20

- First public release: four static weights (Light 300 / Regular 400 /
  Medium 500 / Bold 700), TTF + OTF, GB2312 WOFF2 subset, 32,198 glyphs.
