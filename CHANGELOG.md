# Changelog

All notable changes to HowsenLiu Fangrun are documented here.
This project adheres to [Semantic Versioning](https://semver.org/).

## [2.000] — 2026-11-20

### Added

- **Three-axis variable font** `HowsenLiuFangrun-VF.ttf`
  - `wght` 100–700 (default 400)
  - `wdth` 75–105 (default 100)
  - `opsz` 12–72 (default 16)
- **Eight compatible masters** (30 MB each, rebuilt on demand — not committed to the repo,
  see `sources/masters/README.txt`): four native weights (Light 100 / Regular 400 /
  Medium 500 / Bold 700), two width masters (75 / 105), two optical-size masters (12 / 72).
- `sources/HowsenLiuFangrun.designspace` — three axes, eight sources, eight named instances.
- **Static companions** for software without variable-axis support:
  four static TTFs plus `HowsenLiuFangrun-TTC.ttc` (static collection for older WPS).
- Web build: `HowsenLiuFangrun-VF.woff2` (full, 53.4 MB), `HowsenLiuFangrun-VF-subset.woff2`
  (GB2312, 8,470 glyphs) and `HowsenLiuFangrun-VF-demo.woff2` (page demo, 752 glyphs, 0.61 MB).
- `qa/QA-插值兼容性报告.md` — automated proof of point-structure identity across all masters.
- `specimen/` — eight specimen plates rendered directly from the variable font.

### Design

- Every corner and terminal gets one circular fillet of 70/1000 em. The fillet plan is
  computed once on Regular and replayed on every master with the
  same trim distance and the same arc-segment count, so all eight masters keep an identical
  point structure (contour count, point count, point order, on/off flags).
- Weight axis comes from **native Noto Sans SC variable instances**, not from offsetting a
  single skeleton, so stems keep their true drawings at every weight.
- `opsz` is implemented as stroke compensation (± borrow from the neighbouring native weight)
  plus a 2 % optical scale at the small end; `wdth` is a proportional horizontal scale.
  Both are structure-preserving transforms, so interpolation stays exact.
- Coverage kept at 33,225 code points: Extension B and part of the compatibility block,
  which have no native variable source, are synthesised from the previous Regular outline
  with point-wise offsets (same structure, same point count).

### Changed

- Metadata rewritten for the variable build: `fvar` (three axes, eight named instances),
  `STAT` (three axes with Light/Regular/Medium/Bold, Condensed/Normal/Expanded,
  Caption/Text/Display labels), OS/2, name table IDs 0–17, `HVAR` for advance widths.
- Version bumped to 2.000; family name in the variable build is
  `HowsenLiu Fangrun`, subfamily `Variable`.
- Heavy deliverables (`HowsenLiuFangrun-VF.ttf` 140 MB, `HowsenLiuFangrun-TTC.ttc` 120 MB)
  ship as GitHub Release assets, because both exceed the 100 MB per-file limit.

### Known limitations

- No TrueType hinting.
- No Latin kerning (`kern` / GPOS pairs).
- Simplified/Traditional regional variants not separated (no `locl`).
- Width axis is a proportional horizontal scale; stems get proportionally lighter at 75.

## [1.000] — 2026-11-20

- First public release: four static weights (Light 300 / Regular 400 / Medium 500 / Bold 700),
  TTF + OTF, GB2312 WOFF2 subset, 32,198 glyphs, SIL OFL 1.1.
