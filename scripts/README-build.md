# 构建说明（8 母版 → 三轴可变字体）

```bash
pip install fonttools skia-pathops ufoLib2 ufo2ft brotli Pillow
```

按顺序运行：

| 脚本 | 作用 | 产物 |
|---|---|---|
| `vf_lib.py` | 几何核心：二次点列 ↔ 段、圆角计划、结构保持变换、补字点位移 | — |
| `01_build_masters.py` | 从 Noto Sans SC 可变字体取 100/400/500/700 原生实例，统一圆角（70/1000 em），导出 8 个同源母版 | `build/masters/*.ttf` |
| `02_build_vf.py` | 生成 designspace 与 gvar，写入 fvar / STAT / name / OS2 | `build/HowsenLiuFangrun-VF.ttf` |
| `14_fix_fvar_names.py` | 对齐 fvar 轴名与 8 个命名实例的 nameID（一般 02 已内置，此脚本用于修补旧产物） | 原地修改 VF |
| `03_instances.py` | 4 个静态实例、TTC 集合包 | `build/static/` |
| `17_rebuild_web.py` | WOFF2：全量、GB2312 子集（8,470 字形）、页面演示子集（752 字形） | `build/webfonts/` |
| `04_specimens.py` | 用可变字体本身渲染样张 | `build/specimen/` |
| `05_qa.py` | 结构一致性、6 组中间实例、面积单调性、字宽比、覆盖率校验 | `build/QA-插值兼容性报告.md` |
| `06_package.py` | 按发布包规则组装三段目录与压缩包 | `发布包/` |

## 母版与轴

```
wght 100 ── 400 ── 500 ── 700      (wdth 100, opsz 16)
wdth 75  ── 100 ── 105              (wght 400, opsz 16)
opsz 12  ── 16（默认，与 Regular 同位）── 72  (wght 400, wdth 100)
```

- 字重 = 原生实例，骨架与笔画来自 Noto Sans SC 可变字体，不做偏移生成；
- 字宽 = Regular 的横向等比缩放（x 与 advance 同步乘系数）；
- 光学 = 向相邻原生字重借笔画（12 号借 Medium 41%，72 号借 Light 29%），12 号再做 2% 字面放大。

## 为什么插值安全

1. 所有母版的 glyph 结构来自同一份 TTF 点列，点数为先天一致；
2. 圆角计划只在 Regular 上算一次（哪些交接点圆角、切距 `t`、弧段数 `K`），
   其余母版按同一份计划套用，只重算几何、不重算结构；
3. 圆角弧由固定 `K` 段二次曲线表示，每段恰好产生 1 个控制点 + 1 个 on-curve 点；
4. 字宽/光学母版只做点坐标的仿射或加权，点数与点序不动；
5. 补字（ExtB 等）从旧版 Regular 轮廓按点位移合成四字重，同样逐点对应。

`05_qa.py` 会对 8 个母版逐字比对 `numberOfContours / 点数 / on-off 标记 / endPtsOfContours`，
并在 12 个中间坐标上重新实例化复核，报告写入 `qa/`。
