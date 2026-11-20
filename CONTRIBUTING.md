# 参与贡献

字体是手工活，欢迎 Issue 与 Pull Request。

## 可以提什么

- 字形问题：错字、笔画粘连、断线、区域字形不当（请附字符、字号、截图）
- 插值问题：某个字在中轴位置上扭曲、塌陷（请附坐标值）
- 字符缺漏：常用字缺失、符号缺失
- 文档、网页、样张的修正

## 不要动的地方

- **母版结构**：每个字符在 8 个母版上的轮廓数、点数、点序、on/off 标记必须一致。
  修改任何母版轮廓时，必须同步修改全部 8 个母版，并保证点数相同。
- **保留字体名**：`HowsenLiu Fangrun` / `柳皓升方润黑体` 是保留名，衍生版请改名。
- **授权**：本项目为 SIL OFL 1.1，PR 默认按同一授权提交。

## 提 PR 的流程

1. 先开 Issue 说明问题与字符；
2. 改动后本地跑一遍：

```bash
cd scripts
python 01_build_masters.py
python 02_build_vf.py
python 05_qa.py
```

3. `qa/QA-插值兼容性报告.md` 的「结构不一致」必须为 0；
4. PR 里写清改了哪些字、改了哪些母版、点数是否变化。

## 命名约定

- 中文名：柳皓升方润黑体
- 英文名：HowsenLiu Fangrun
- PostScript：`HowsenLiuFangrun-VF`（可变）/ `HowsenLiuFangrun-{Style}`（静态）

## 联系方式

- 邮箱：Musicboss@yeah.net
- 仓库：https://github.com/HowsenLiu/HowsenLiuFangrun
