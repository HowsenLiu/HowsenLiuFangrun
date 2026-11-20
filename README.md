<div align="center">

# HowsenLiu Fangrun Variable · 柳皓升方润黑体

**A three-axis CJK variable typeface — one skeleton, one rounding rule, 33,128 glyphs.**

[![License: SIL OFL 1.1](https://img.shields.io/badge/license-SIL%20OFL%201.1-blue.svg)](LICENSE)
[![Axes](https://img.shields.io/badge/axes-wght%20%C3%97%20wdth%20%C3%97%20opsz-orange.svg)](#axes)
[![Glyphs](https://img.shields.io/badge/glyphs-33%2C128-brightgreen.svg)](#character-coverage)

[简体中文说明](README.zh-CN.md)

</div>

---

![Specimen](specimen/01-overview.png)

## About

**HowsenLiu Fangrun** (柳皓升方润黑体) is built on a square, architectural skeleton where
**every stroke corner and terminal is softened with the same radius (70/1000 em)**.
This release turns it into a **variable font** organised the way SF Pro is:
one weight axis, one width axis, one optical-size axis — driven by **eight masters that
share an identical outline structure**.

Designed by **Howsen Liu (柳皓升)**. Released under the **SIL Open Font License 1.1** —
free for personal and commercial use, modification and redistribution.

## Axes

| Axis | Range | Default | Behaviour |
|---|---|---|---|
| `wght` | 100 → 700 | 400 | Stroke weight. Native masters at Light 100, Regular 400, Medium 500, Bold 700 |
| `wdth` | 75 → 105 | 100 | Horizontal width. 75 condensed, 100 normal, 105 expanded |
| `opsz` | 12 → 72 | 16 | Optical size. Near 12: heavier strokes, larger counters. Near 72: finer strokes, refined details |

## Why the interpolation never breaks

- **Eight masters**: four native weights plus two width masters and two optical-size masters.
- For every character, **contour count, point count, point order and on/off flags are identical
  across all eight masters**.
- The corner-fillet plan is computed **once** on Regular and applied to every master with the
  same trim distance and the same number of arc segments.
- Verification: [`qa/QA-插值兼容性报告.md`](qa/QA-插值兼容性报告.md) — 33,128 glyphs,
  structural mismatches: **0**.

The result is a `gvar` where every point has a defined delta everywhere in the design space;
no shifting, folding or collapse at intermediate positions.

## Files

| Path | |
|---|---|
| `HowsenLiuFangrun-VF.ttf` (Release asset) | Three-axis variable font, 140 MB — above GitHub's 100 MB per-file limit |
| `fonts/webfonts/HowsenLiuFangrun-VF.woff2` | Compressed web build, full charset |
| `fonts/webfonts/HowsenLiuFangrun-VF-subset.woff2` | Web subset (GB2312 common characters, 8,470 glyphs) |
| `fonts/webfonts/HowsenLiuFangrun-VF-demo.woff2` | Tiny demo subset used by this site (752 glyphs, 0.61 MB) |
| `fonts/ttf/HowsenLiuFangrun-{Light,Regular,Medium,Bold}.ttf` | Static weights for software without variable-axis support |
| `HowsenLiuFangrun-TTC.ttc` (Release asset) | Static collection, 120 MB, for legacy WPS / older systems |
| `sources/masters/README.txt` | The eight masters (30 MB each) are not in the repo; rebuild with one command |
| `sources/HowsenLiuFangrun.designspace` | Designspace (three axes, eight sources) |
| `scripts/*.py` | Reproducible build pipeline |
| `specimen/*.png` | Specimens |

## Install

**Windows** — select the `.ttf` files → right-click → *Install*.
**macOS** — double-click → *Install Font*.
**Linux**

```bash
mkdir -p ~/.local/share/fonts
cp fonts/ttf/*.ttf ~/.local/share/fonts     # static weights
# the variable font comes from the Release; cp it into the same folder
fc-cache -f -v
```

For older WPS or software that ignores `fvar`, install `HowsenLiuFangrun-TTC.ttc`
to get all four static weights in one file.

## Web usage

```css
@font-face {
  font-family: "HowsenLiu Fangrun VF";
  src: url("fonts/webfonts/HowsenLiuFangrun-VF.woff2") format("woff2");
  font-weight: 100 700;
  font-stretch: 75% 105%;
  font-display: swap;
}

h1 { font-family: "HowsenLiu Fangrun VF";
     font-variation-settings: "wght" 600, "wdth" 100, "opsz" 48; }

p  { font-family: "HowsenLiu Fangrun VF"; font-optical-sizing: auto; }
```

## Build from source

```bash
pip install fonttools skia-pathops ufoLib2 ufo2ft brotli Pillow

cd scripts
python 01_build_masters.py    # eight compatible masters
python 02_build_vf.py         # designspace + gvar → VF
python 03_instances.py        # statics + TTC + WOFF2
python 04_specimens.py        # specimens
python 05_qa.py               # compatibility report
```

The masters are **native instances** of the Noto Sans SC variable font at 100/400/500/700 —
not one weight offset into many — so the skeleton is genuinely shared. Rounding is then
applied through a single shared fillet plan.

## Character coverage

33,225 code points / 33,128 glyphs:

| Range | Count |
|---|---|
| CJK Unified Ideographs (Simplified and Traditional) | 20,976 |
| CJK Extension A | 6,582 |
| CJK Extension B | 2,108 |
| CJK Extensions C–F | 198 |
| CJK Compatibility Ideographs | 366 |
| Kangxi Radicals + CJK Radicals Supplement | 329 |
| Kana / Bopomofo / Fullwidth forms | 593 |
| Latin (Basic, Latin-1, Extended) | 244 |
| Greek + Cyrillic | 115 |
| Symbols (punctuation, arrows, math, currency, box drawing, shapes) | 1,714 |

Extension B and part of the compatibility block have no native variable source in the new
masters; they are synthesised from the previous Regular outline with point-wise offsets,
keeping the same structure so coverage matches v1.000.

## License and attribution

**SIL Open Font License 1.1.** Commercial use, modification and redistribution are permitted.
Derivatives must stay under the OFL and may not use the reserved name `HowsenLiu Fangrun`.

When redistributing, **keep the original skeleton attribution**:

- Glyph skeleton: **Noto Sans CJK SC / Noto Sans SC**, Copyright 2014–2021 Adobe
  (<http://www.adobe.com/>), SIL OFL 1.1.
- Original skeleton design: **Ryoko NISHIZUKA, Paul D. Hunt, Sandoll Communications**.

Changes in this project: uniform corner rounding (70/1000 em, 正圆弧 1.0), three-axis master
construction and interpolation-structure unification, static instances and TTC packaging,
naming and metadata. Design: **Howsen Liu (柳皓升)**.

## Known limitations

- No TrueType hinting.
- No Latin kerning yet.
- Regional SC/TC glyph variants are not separated (no `locl`).
- The width axis is a proportional horizontal scale, so stems get proportionally lighter at 75.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) and [FONTLOG.txt](FONTLOG.txt).
