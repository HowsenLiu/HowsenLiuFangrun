<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logo-mark-dark.png">
  <img src="logo-mark.png" alt="柳皓升方润黑体" height="72">
</picture>

# 柳皓升方润黑体 · HowsenLiu Fangrun

**方正骨架，圆润收口 —— 一款为屏幕与印刷打磨的中文无衬线字体。**

[![Version](https://img.shields.io/badge/version-2.000-111111.svg)](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest)
[![License](https://img.shields.io/badge/license-免费%20·%20个人%20%26%20商用-111111.svg)](LICENSE)
[![Glyphs](https://img.shields.io/badge/glyphs-33%2C128-6a737d.svg)](#字符支持)

[English](README.md) · [字体官网](https://howsenliufangrun.pages.dev) · [GitHub](https://github.com/HowsenLiu/HowsenLiuFangrun)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="specimen/hero-dark.gif">
  <img src="specimen/hero.gif" alt="柳皓升方润黑体样张轮播 —— 中文、English、日本語与符号" width="100%">
</picture>

</div>

柳皓升方润黑体是一款在人文观感与几何骨架之间取得平衡的中文无衬线字体。整体以略方的
建筑感骨架为底，在每一处笔画交接与端点做同一半径的圆角处理：结构方正，细节柔和，
长句阅读干净，标题醒目。字体覆盖简繁中文、拉丁及欧洲带调字母、希腊字母、西里尔字母、
日文假名、注音符号、阿拉伯数字与各类常用标点符号。

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

### Release 附件

| 版本 | 格式 · 体积 | 下载 |
|---|---|---|
| 可变字体 | `.ttf` · 140.0 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.ttf) |
| 静态字重包 | `.zip` · 47.7 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-Static-TTF.zip) |
| 静态集合包 | `.ttc` · 114.5 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.ttc) |
| 网页字体包 | `.zip` · 65.7 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-WOFF2.zip) |
| 可变完整包 | `.zip` · 124.2 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-VF.zip) |
| 集合压缩包 | `.zip` · 47.2 MB | [获取](https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest/download/HowsenLiuFangrun-TTC.zip) |

## 字符支持

| 文字 | 支持情况 |
|:-:|:-:|
| 汉字 | 覆盖 GBK 全集、GB18030 一级、Big5 繁体；共计 33,128 字形 / 33,225 码位 |
| 拉丁与欧洲字母 | 基础拉丁 + 带变音字母（À Á Â Ä Ç É È Ê Ë Ñ Ó Ô Ö Ú Ü ã õ ç 等），可支持英、法、德、西、葡等语言 |
| 希腊 / 西里尔 | 基础希腊字母、西里尔字母 |
| 日文假名 | 平假名、片假名 |
| 注音符号 | 注音字母 ㄅㄆㄇㄈ |
| 数字 | 阿拉伯数字 0–9 |
| 标点符号 | 中西文标点、箭头、几何形、货币符号与常用符号 |

## 可变轴

| 轴 | 范围 · 默认值 |
|:-:|:-:|
| `wght` 厚度 | 100–700 · 400 |
| `wdth` 宽窄 | 75–105 · 100 |
| `opsz` 光学尺寸 | 12–72 · 16 |

不支持可变轴的软件可使用配套静态字体：Light / Regular / Medium / Bold 四款 TTF 与
TTC 集合包。

## 注意事项

- 简繁区域变体未做区分（无 `locl` 特性）。
- 无 TrueType 屏幕提示（hinting）；无拉丁字距调整（`kern` / GPOS 配对）。
- 宽窄轴为等比例横向缩放，75 缩窄时笔画会成比例变细。

## 样张

![字重展示](specimen/01-weights.png)

![柳字圆角细节](specimen/02-liu.png)

![正文排版](specimen/03-text.png)

![拉丁与符号](specimen/04-latin.png)

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
- 字体官网：[howsenliufangrun.pages.dev](https://howsenliufangrun.pages.dev)
- X / Twitter：[@HowsenLiu_](https://x.com/HowsenLiu_)

## 许可证

- **允许**：个人使用与商业使用，嵌入网页、文档、包装、界面与随售产品。
- **禁止**：修改字体文件与技术参数、提取轮廓制作衍生字体、单独再分发或转售、用于
  AI 模型训练；仅作者本人可修改源码与字体文件。
- 完整条款见 [LICENSE](LICENSE)；原始骨架署名（Noto Sans CJK SC / Noto Sans SC，
  Adobe，SIL OFL 1.1）按要求完整保留。

---

<div align="center">

Copyright © 2026 **柳皓升 Howsen Liu** · 版本 2.000 · [变更记录](CHANGELOG.md)

</div>
