母版不随仓库分发（8 个 × 30 MB）。
需要重建时，在装有 fontTools / skia-pathops / ufo2ft 的环境里执行：

    python scripts/01_build_masters.py      # 由 Noto Sans SC VF 取 100/400/500/700 四实例，
                                            # 统一圆角，派生 wdth75 / wdth105 / opsz12 / opsz72
    python scripts/02_build_vf.py           # 生成 HowsenLiuFangrun-VF.ttf
    python scripts/03_instances.py          # 静态 TTF + TTC + WOFF2
    python scripts/05_qa.py                 # 插值兼容性报告

母版文件名：HowsenLiuFangrun-{Light,Regular,Medium,Bold,Cond75,Exp105,Opt12,Opt72}-master.ttf
依赖的唯一外部源字体：C:\Windows\Fonts\NotoSansSC-VF.ttf（Noto Sans SC，SIL OFL 1.1）。
