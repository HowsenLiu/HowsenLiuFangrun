<div align="center">

<a href="#gh-light-mode-only">
  <img src="logo-mark.png" alt="柳皓升方润黑体" height="72">
</a>
<a href="#gh-dark-mode-only">
  <img src="logo-mark-dark.png" alt="柳皓升方润黑体" height="72">
</a>

# 柳皓升方润黑体 · HowsenLiu Fangrun

**方折骨架，圆润收口 —— 一款为屏幕与印刷打磨的中文无衬线字体。**

**柳皓升方润黑体 · 柳皓升方潤黑體 · HowsenLiu Fangrun · 柳皓升方潤ゴシック · 柳皓升방운고딕**

[![Version](https://img.shields.io/badge/version-2.000-1d1d1f.svg)](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest)
[![License](https://img.shields.io/badge/license-OFL%201.1-1d1d1f.svg)](LICENSE)
[![Glyphs](https://img.shields.io/badge/glyphs-44%2C731-6a737d.svg)](#字符支持)

[![English](https://img.shields.io/badge/English-README-1d1d1f.svg)](README.md)
[![GitHub](https://img.shields.io/badge/GitHub-仓库-1d1d1f.svg)](https://github.com/HowsenLiu/HowsenLiuFangrun)
[![官网](https://img.shields.io/badge/website-howsenliufangrun.pages.dev-1d1d1f.svg)](https://howsenliufangrun.pages.dev/)

<img src="specimen/hero.png" alt="柳皓升方润黑体样张 —— 简体中文、繁體中文、English、日本語、한국어与符号" width="100%">

</div>

柳皓升方润黑体是一款在人文观感与几何骨架之间取得平衡的中文无衬线字体。整体以略方的
建筑感骨架为底，在每一处笔画交接与端点做同一半径的圆角处理：结构方折，细节柔和，
长句阅读干净，标题醒目。字体覆盖简繁中文、韩文谚文（全部预组音节与字母）、拉丁及欧洲
带调字母、希腊字母、西里尔字母、日文假名、注音符号、上标 / 下标 / 修饰字母、阿拉伯
数字与各类常用标点符号，共计 **44,731 字形 / 44,828 码位**。

## 下载安装

- 点击 [Releases](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest) 可直接下载
  安装文件包：
  - `.ttf` / `.ttc` 文件用于桌面端安装，打开文件后按系统提示安装即可；
  - `.woff2` 为网页字体格式，供网站开发人员使用。
- 按系统安装：
  - **Windows** — 选中 `.ttf` 文件 → 右键 → *安装*。
  - **macOS** — 双击字体文件 → *安装字体*。
  - **Linux**

    ```bash
    mkdir -p ~/.local/share/fonts
    cp fonts/ttf/*.ttf ~/.local/share/fonts
    fc-cache -f -v
    ```
- 不支持可变轴的旧版 WPS / 老软件，可下载 TTC 集合包，一次装入四款静态字重。
- 可变、静态、TTC 三套文件使用各自独立的族名与 PostScript 名，同时安装不会被字体管理器判为重复而互相覆盖。

### Release 附件

所有安装包均按仓库 OFL 1.1 协议免费下载。

| 分类 | 安装包 | 文件 | 格式 · 体积 | 下载 |
|---|---|---|---|---|
| 桌面端 | 可变字体 | `HowsenLiuFangrun-VF.ttf` | TTF · 184.1 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.ttf) |
| 桌面端 | 可变完整包 · VF + 全量 WOFF2 + FONTLOG | `HowsenLiuFangrun-VF.zip` | ZIP · 151.4 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip) |
| 桌面端 | 静态字重包 · Light / Regular / Medium / Bold | `HowsenLiuFangrun-Static-TTF.zip` | ZIP · 56.5 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip) |
| 桌面端 | TTC 集合包 · 四款静态字重单文件 | `HowsenLiuFangrun-TTC.ttc` | TTC · 150.4 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.ttc) |
| 桌面端 | 集合压缩包 | `HowsenLiuFangrun-TTC.zip` | ZIP · 55.9 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip) |
| 网页嵌入 | 网页字体包 · 全量 / 子集 / 演示 WOFF2 | `HowsenLiuFangrun-WOFF2.zip` | ZIP · 80.2 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip) |
| 协议 | OFL 1.1 完整协议文本（各压缩包内已附） | `LICENSE-OFL-1.1.txt` | TXT · 4.5 KB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/LICENSE-OFL-1.1.txt) |

### 给 AI 助手的自取提示词

每个安装包对应一段独立提示词，把需要的那段粘贴给 AI 助手即可，直达下载地址已写在其中。

**可变完整包（VF）**

```text
请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」可变字体包，安装到我的项目。
直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip
仓库：https://github.com/HowsenLiu/HowsenLiuFangrun
包内为可变字体 HowsenLiuFangrun-VF.ttf，含字重 wght 100–700、宽度 wdth 75–105、光学尺寸 opsz 12–72 三轴。
按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。
```

**静态字重包（Static TTF）**

```text
请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」静态字重包，安装到我的项目。
直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip
仓库：https://github.com/HowsenLiu/HowsenLiuFangrun
包内含 Light / Regular / Medium / Bold 四款静态 TTF。
按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。
```

**TTC 集合包**

```text
请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」TTC 集合包，安装到我的项目（兼容旧版 WPS 与老系统）。
直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip
仓库：https://github.com/HowsenLiu/HowsenLiuFangrun
包内为单文件 TTC 集合，一次装入四款静态字重。
按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。
```

**网页字体包（WOFF2）**

```text
请从 GitHub 获取「柳皓升方润黑体 / HowsenLiu Fangrun」网页 WOFF2 包，嵌入我的网站。
直达下载：https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip
仓库：https://github.com/HowsenLiu/HowsenLiuFangrun
包内为网站嵌入用 WOFF2 压缩版本。
按仓库 LICENSE（SIL OFL 1.1）授权使用：可免费商用，也允许修改与制作衍生字体；衍生版本须继续以 OFL 1.1 发布，并保留署名与许可文本；字体文件不得脱离软件单独售卖。
```

## 字符支持

| 文字 / 区块 | 覆盖情况 |
|---|---|
| 汉字 · 简繁中文 | GBK 全集、GB 18030 一/二级汉字、Big5 繁体；20,976 个统一表意文字 + 6,582 个扩展 A 汉字 |
| 韩文谚文 | 全部 11,172 个预组音节（가–힣）、254 个 Jamo 字母、扩展 A/B、兼容字母与半宽形式 |
| 日文假名 | 平假名 93 个、片假名 96 个 |
| 拉丁与欧洲字母 | 基础拉丁 + 拉丁扩展 A/补充区与变音字母（À Á Â Ä Ç É È Ê Ë Ñ Ó Ô Ö Ú Ü ã õ ç 等），可支持英、法、德、西、葡、意等语言 |
| 希腊 / 西里尔 | 基础希腊字母（49 码位）、西里尔字母（66 码位） |
| 注音符号 | 43 个注音字母 ㄅㄆㄇㄈ |
| 数字与字母标记 | 阿拉伯数字 0–9、罗马数字 Ⅰ–Ⅹ、上标 / 下标 / 修饰字母 |
| 标点符号 | 中西文标点、箭头、几何形、货币符号、版权 / 商标标记与常用界面符号 |
| **合计** | **44,731 字形 / 44,828 码位** |

## 可变轴

| 轴 | 范围 · 默认值 |
|:-:|:-:|
| `wght` 厚度 | 100–700 · 400 |
| `wdth` 宽窄 | 75–105 · 100 |
| `opsz` 光学尺寸 | 12–72 · 16 |

不支持可变轴的软件可使用配套静态字体：Light / Regular / Medium / Bold 四款 TTF 与
TTC 集合包。

## OpenType 特性

可变字体与四款静态配套字体携带同一套 GSUB / GPOS 特性集。

### 替换特性（GSUB）

| 特性 | 标签 | 作用 |
|---|---|---|
| 标准连字 | `liga` | 默认连字 |
| 自由连字 | `dlig` | 可选连字 |
| 字符合成 / 分解 | `ccmp` | 组合或拆分复合字符 |
| 地区字形 | `locl` | 按文字体系切换地区变体 |
| 全角变体 | `fwid` | 全角字形替换 |
| 半角变体 | `hwid` | 半角字形替换 |
| 比例宽度变体 | `pwid` | 比例宽度字形替换 |
| 竖排变体 | `vert` / `vrt2` | 竖排直立替代字形 |
| 注音假名 | `ruby` | 注音（ruby）小号字形 |
| 历史字形 | `hist` | 旧式 / 历史字形 |
| 备用字形访问 | `aalt` | 暴露某一字形的全部备用形 |

### 定位特性（GPOS）

| 特性 | 标签 | 作用 |
|---|---|---|
| 横向字距 | `kern` | 假名、中文标点与拉丁附加符号的配对字距（845 对） |
| 竖向字距 | `vkrn` | 竖排配对字距（560 对） |
| 附加符号定位 | `mark` | 附加符号对基线 / 对附加符号的定位 |
| 竖排定位 | `vert` | 竖排排版定位 |
| 宽度感知定位 | `halt` `palt` `vhal` `vpal` | 半角 / 比例宽度定位表；本版本仅保留注册标签，未附加额外调整规则 |

### 字体表

- `fvar` / `STAT` / `gvar` / `HVAR` / `VVAR` —— 可变轴与变化元数据
- `cmap` —— Unicode 映射（format 4 + format 12），另有 `BASE`、`GDEF`、`hmtx`、`vmtx`、`gasp`
- 不含 Apple AAT 表（`mort` / `morx`）。

## 注意事项

- 简繁区域变体除保留的地区字形外，未通过 `locl` 做额外拆分。
- 无 TrueType 屏幕提示（hinting）；拉丁基础字母对未做专门字距调整，保留的 `kern` / `vkrn` 配对覆盖假名、中文标点与附加符号。
- 宽窄轴为等比例横向缩放，75 缩窄时笔画会成比例变细。

## 样张

![多语言封面](specimen/hero.png)

![字重轴](specimen/spec-weights.png)

![多语言版面](specimen/spec-multilingual.png)

![正文排版](specimen/spec-text.png)

![字符集](specimen/spec-charset.png)

## 网页嵌入

```css
@font-face {
  font-family: "HowsenLiu Fangrun";
  src: url("fonts/webfonts/HowsenLiuFangrun-VF-subset.woff2") format("woff2");
  font-weight: 100 700;
  font-display: swap;
}

body { font-family: "HowsenLiu Fangrun", sans-serif; }
```

全字符集 WOFF2 体积较大，随 Release 附件分发；线上页面建议使用仓库内的常用子集，
或按文案自行二次子集化。

## 关于

- 设计：[柳皓升（Howsen Liu）](https://github.com/HowsenLiu)
- 官网：[howsenliufangrun.pages.dev](https://howsenliufangrun.pages.dev/)
- X / Twitter：[@HowsenLiu_](https://x.com/HowsenLiu_)
- 行为守则：[`.github/CODE_OF_CONDUCT.md`](.github/CODE_OF_CONDUCT.md)

## 许可证

本仓库附带 **两份 SIL Open Font License 1.1（OFL 1.1）** 文本：

1. **本字体发布版** —— [`LICENSE`](LICENSE)：Copyright 2014–2021 Adobe and Google LLC
   （Noto Sans CJK SC / Noto Sans SC / Noto Sans KR）；Copyright 2026 柳皓升 Howsen Liu
   （https://github.com/HowsenLiu），以 OFL 1.1 发布。
2. **上游保留源文件** —— [`sources/kr/OFL-NotoSansKR.txt`](sources/kr/OFL-NotoSansKR.txt)：
   内嵌 Noto Sans KR 骨架源文件的原始 OFL 1.1 声明，Copyright 2014–2021 Adobe，
   保留字体名 `Source`，按原文保留未作改动。

使用边界遵循 OFL 1.1 协议原文：可免费用于个人与商业项目，允许修改字形、调整参数与
制作衍生字体。衍生版本必须继续以 OFL 1.1 发布，不得更换为其他许可证，并须保留原始
版权声明、作者署名与许可全文；字体文件不得脱离软件单独售卖。

- **保留字体名**：`HowsenLiu Fangrun`、`柳皓升方润黑体`、`方润黑体`、`Fangrun`；
  衍生修改版不得沿用以上任何名称，需更名后再发布。

### 使用场景对照

| 场景 | 说明 |
|:-:|---|
| ✅ 可直接使用（无需另行授权） | 印刷品（海报、包装、宣传册）、视频字幕与封面、网页字体加载、个人及企业商业物料、设计稿交付 |
| ✅ 可随附分发（须保留署名与 OFL 全文） | 随软件、项目或硬件捆绑分发 |
| ⚠️ 建议事先书面确认 | 将字体嵌入 App / 小程序 / 游戏安装包内部分发；以字体字形为核心元素申请注册商标 |
| ❌ 禁止 | 将字体文件本身单独打包标价出售；删除或篡改原始版权声明与许可文本 |

---

<div align="center">

Copyright © 2026 **柳皓升 Howsen Liu** · 版本 2.000 · [变更记录](CHANGELOG.md)

</div>
