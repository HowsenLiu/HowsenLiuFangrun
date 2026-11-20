# 柳皓升方润黑体 · 可变字体

**HowsenLiu Fangrun Variable** — 中文三轴可变字体：一个骨架，三种呼吸。

[![License: SIL OFL 1.1](https://img.shields.io/badge/license-SIL%20OFL%201.1-blue.svg)](LICENSE)
[![Axes](https://img.shields.io/badge/axes-wght%20%C3%97%20wdth%20%C3%97%20opsz-orange.svg)](#三条轴)
[![Glyphs](https://img.shields.io/badge/glyphs-33%2C128-brightgreen.svg)](#字符覆盖)

[English README](README.md)

---

## 这是什么

柳皓升方润黑体以略方的骨架为底，在每一处笔画交接与端点做**同一半径（70/1000 em）**的圆角处理：
方块结构，圆润收口。这一版把它做成了**三轴可变字体**，对标 SF Pro 的组织方式——
字重、字宽、光学尺寸各一根轴，由 8 个结构完全同源的母版驱动。

| 轴 | 范围 | 默认 | 作用 |
|---|---|---|---|
| `wght` | 100 → 700 | 400 | 笔画粗细。四个原生母版：Light 100 / Regular 400 / Medium 500 / Bold 700 |
| `wdth` | 75 → 105 | 100 | 字宽伸缩。75 窄体、100 标准、105 宽体 |
| `opsz` | 12 → 72 | 16 | 光学尺寸。12 号附近笔画加粗、中宫放大；72 号附近笔画收细、细节精致 |

## 为什么插值不会崩

这是这份字体工程的核心约束：

- **8 个母版**（4 字重 × 1 + 宽度 2 + 光学 2），全部由同一套轮廓结构导出；
- 每个字符在 8 个母版上的**轮廓数、控制点数量、控制点顺序、on/off 标记完全一致**；
- 圆角计划只在 Regular 上计算一次，其余母版按同一份计划（同一 `t`、同一弧段数 `K`）套用；
- 校验结果见 [`qa/QA-插值兼容性报告.md`](qa/QA-插值兼容性报告.md)：33,128 字形，结构不一致 **0**。

因此在 100–700 / 75–105 / 12–72 之间任意取值，gvar 的每个点都有确定的增量，不会出现错位、翻折或塌陷。

## 文件清单

| 路径 | 说明 |
|---|---|
| `HowsenLiuFangrun-VF.ttf`（Release 附件） | 三轴可变字体，140 MB，超 GitHub 单文件 100 MB 上限，随 Release 分发 |
| `fonts/webfonts/HowsenLiuFangrun-VF.woff2` | 网页用压缩版（全字符集） |
| `fonts/webfonts/HowsenLiuFangrun-VF-subset.woff2` | 网页用子集（GB2312 常用字，8,470 字形） |
| `fonts/webfonts/HowsenLiuFangrun-VF-demo.woff2` | 本站演示用极小集（752 字形，0.61 MB） |
| `fonts/ttf/HowsenLiuFangrun-{Light,Regular,Medium,Bold}.ttf` | 四个静态字重，兼容不支持可变轴的软件 |
| `HowsenLiuFangrun-TTC.ttc`（Release 附件） | 静态集合包 120 MB，旧版 WPS / 老系统一次装入四款 |
| `sources/masters/README.txt` | 母版共 8 个 × 30 MB，不随仓库分发；按说明一条命令即可重建 |
| `sources/HowsenLiuFangrun.designspace` | designspace 定义（三轴 + 8 源） |
| `scripts/*.py` | 可复现构建脚本（母版 → 可变字体 → 静态 → 样张 → QA） |
| `specimen/*.png` | 样张 |
| `qa/QA-插值兼容性报告.md` | 插值兼容性与覆盖校验 |

## 安装

**Windows** — 选中 `.ttf` → 右键 → 安装（或「为所有用户安装」）。
安装后可字体列表里搜 `HowsenLiu Fangrun` 或 `柳皓升方润黑体`。

**macOS** — 双击字体文件 → 字体册「安装字体」。

**Linux**

```bash
mkdir -p ~/.local/share/fonts
cp fonts/ttf/*.ttf ~/.local/share/fonts      # 静态字重
# 可变版从 Release 下载后同样 cp 进该目录
fc-cache -f -v
```

**Photoshop / Illustrator / Figma / InDesign** — 系统级安装后，在字重下拉里可直接调 100–700；
支持可变轴的版本还能在字符面板里调宽度与光学尺寸。

**旧版 WPS / 老软件** — 装 `HowsenLiuFangrun-TTC.ttc`（Release 附件），一次得到 Light / Regular / Medium / Bold 四款静态字体。

## 网页用法

```css
@font-face {
  font-family: "HowsenLiu Fangrun VF";
  src: url("fonts/webfonts/HowsenLiuFangrun-VF.woff2") format("woff2");
  font-weight: 100 700;
  font-stretch: 75% 105%;
  font-display: swap;
}

h1 {
  font-family: "HowsenLiu Fangrun VF";
  font-variation-settings: "wght" 600, "wdth" 100, "opsz" 48;
}

/* 交给浏览器按字号自动选光学尺寸 */
p {
  font-family: "HowsenLiu Fangrun VF";
  font-optical-sizing: auto;
}
```

`font-stretch: 75% 105%` 对应 `wdth`；`font-optical-sizing: auto` 对应 `opsz`。
全字符集 woff2 体积较大，页面里建议用 `HowsenLiuFangrun-VF-subset.woff2`（GB2312 常用字），
或按自己的文案二次子集：

```bash
pyftsubset HowsenLiuFangrun-VF.ttf \
  --text-file=your-text.txt --flavor=woff2 \
  --output-file=my-subset.woff2
```

## 从源码重建

```bash
pip install fonttools skia-pathops ufoLib2 ufo2ft brotli Pillow

cd scripts
python 01_build_masters.py      # 8 个同源母版（约 5 分钟）
python 02_build_vf.py           # designspace + gvar → HowsenLiuFangrun-VF.ttf
python 03_instances.py          # 4 个静态 TTF + TTC + WOFF2
python 04_specimens.py          # 样张
python 05_qa.py                 # 插值兼容性报告
```

母版来自 **Noto Sans SC 可变字体**的原生实例（100/400/500/700），
不是「一个母版偏移出所有字重」，所以骨架天然同源；圆角化由一个共享的圆角计划统一施加。

## 字符覆盖

33,225 个码位 / 33,128 个字形：

| 区块 | 数量 |
|---|---|
| 基本汉字（简繁） | 20,976 |
| 扩展 A | 6,582 |
| 扩展 B | 2,108 |
| 扩展 C–F | 198 |
| 兼容汉字 | 366 |
| 康熙部首 / CJK 部首补充 | 329 |
| 假名 / 注音 / 全角形式 | 593 |
| 拉丁（基本 / Latin-1 / 扩展） | 244 |
| 希腊 / 西里尔 | 115 |
| 符号（标点、箭头、数学、货币、制表、图形） | 1,714 |

说明：扩展 B 与部分兼容区字符在新母版里没有原生可变源，
由旧版 Regular 轮廓按点位移合成四字重（结构仍严格一一对应），
以保证与上一版 v1.000 的字符覆盖一致。

## 授权与署名

**SIL Open Font License 1.1** — 可免费用于个人与商业项目，可修改、可再分发；
衍生字体须继续使用 OFL 1.1，且不得使用保留字体名 `HowsenLiu Fangrun`。

分发、再发布、二次开发时**必须保留原始骨架作者署名**：

- 字形骨架：**Noto Sans CJK SC / Noto Sans SC**，Copyright 2014–2021 Adobe
  （<http://www.adobe.com/>），SIL OFL 1.1；
- 原骨架设计：**Ryoko NISHIZUKA、Paul D. Hunt、Sandoll Communications**。

本项目完成的改动：全轮廓统一圆角化（70/1000 em，正圆弧 1.0）、
三轴母版构建与插值结构统一、静态实例与 TTC 打包、命名与元数据。
设计：**柳皓升 Howsen Liu**。

## 已知限制

- 无 TrueType 指令（hinting），极小字号下依赖渲染器的自动微调；
- 中西文暂无 kerning；
- 简繁地区字形未分离（未做 `locl`），繁体字以简体字形呈现；
- 宽度轴为横向等比缩放，窄体（75）竖画会相应变细，属设计取舍。

## 变更

见 [CHANGELOG.md](CHANGELOG.md) 与 [FONTLOG.txt](FONTLOG.txt)。
