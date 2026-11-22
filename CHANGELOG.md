# Changelog

All notable changes to HowsenLiu Fangrun are documented here.

## [2.000] — 2026-11-22 revision

### Added

- **81 superscript / subscript / modifier letters** synthesized from the
  masters; the variable font and all static / TTC / WOFF2 downstream builds
  were rebuilt from the updated masters.
- Rebuilt specimen set: multilingual cover, weight axis, multilingual board,
  body text and character-set sheet under `specimen/`.

### Design

- Coverage: **44,828 code points / 44,731 glyphs**.

## [2.000] — 2026-11-21 revision

### Added

- **Korean Hangul** merged from the Noto Sans KR skeleton (SIL OFL 1.1): all
  11,172 precomposed syllables (가–힣), jamo, extended jamo A/B, compatibility
  letters and halfwidth forms.

### Design

- Fillet radius raised from 70 to 88/1000 em, with a lower turn-angle
  threshold, so corners and terminals are rounder across CJK and Hangul alike.
- Coverage: 44,752 code points / 44,655 glyphs (pre-marks build).

### Attribution

- Original skeleton notices now cover Noto Sans CJK SC / Noto Sans SC and
  Noto Sans KR (Copyright 2014–2021 Adobe and Google LLC, SIL OFL 1.1); the OFL
  terms themselves are unchanged.

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
- License updated to SIL Open Font License 1.1 (OFL 1.1): free for
  personal and commercial use; modification and derivatives are permitted
  under OFL terms — see [LICENSE](LICENSE).

### Known limitations

- No TrueType hinting.
- No Latin kerning (`kern` / GPOS pairs).
- Simplified/Traditional regional variants not separated (no `locl`).
- Width axis is a proportional horizontal scale; stems get proportionally
  lighter at 75.

## [1.000] — 2026-11-20

- First public release: four static weights (Light 300 / Regular 400 /
  Medium 500 / Bold 700), TTF + OTF, GB2312 WOFF2 subset, 32,198 glyphs.
