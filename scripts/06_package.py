"""06  按既有规则组装发布包（1_GitHub仓库上传 / 2_网页部署 / 3_字体下载 / 4_样张预览）"""
from __future__ import annotations

import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, 'build')
PKG = os.path.join(os.path.dirname(ROOT), '发布包')
SCRIPTS = os.path.join(ROOT, 'scripts')
OLD = (r'C:\Users\12784\Desktop\字体\柳皓升方润黑体-发布包\发布包'
       r'\1_GitHub仓库上传\sources\charset')

GH = os.path.join(PKG, '1_GitHub仓库上传')
SITE = os.path.join(PKG, '2_网页部署_CloudflarePages')
DL = os.path.join(PKG, '3_字体下载')
PREVIEW = os.path.join(PKG, '4_样张预览')

STATIC = ['Light', 'Regular', 'Medium', 'Bold']
MASTERS = ['Light', 'Regular', 'Medium', 'Bold', 'Cond75', 'Exp105', 'Opt12', 'Opt72']


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def cp_tree(src, dst):
    os.makedirs(dst, exist_ok=True)
    for name in os.listdir(src):
        s = os.path.join(src, name)
        d = os.path.join(dst, name)
        if os.path.isdir(s):
            cp_tree(s, d)
        else:
            cp(s, d)


def mkzip(path, files):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for src, arc in files:
            z.write(src, arc)
    print('  zip', os.path.basename(path), f'{os.path.getsize(path) / 1e6:.1f} MB')


def main():
    # ---------------- 1 GitHub
    os.makedirs(GH, exist_ok=True)
    for style in STATIC:
        cp(os.path.join(BUILD, 'static', f'HowsenLiuFangrun-{style}.ttf'),
           os.path.join(GH, 'fonts', 'ttf', f'HowsenLiuFangrun-{style}.ttf'))
    # VF（140 MB）与 TTC（120 MB）超 GitHub 单文件 100 MB 上限，只走 Release，不进仓库
    os.makedirs(os.path.join(GH, 'fonts', 'variable'), exist_ok=True)
    with open(os.path.join(GH, 'fonts', 'variable', 'README.txt'), 'w', encoding='utf-8') as fh:
        fh.write(
            'HowsenLiuFangrun-VF.ttf 约 140 MB，超过 GitHub 单文件 100 MB 上限，\n'
            '因此不作为仓库文件提交，而是挂在 Release 附件里：\n\n'
            '    https://github.com/HowsenLiu/HowsenLiuFangrun/releases/latest\n\n'
            '需要直链时可复制 Release 附件地址。\n'
            '若一定要放进仓库，请开启 Git LFS 后单独提交：\n\n'
            '    git lfs track "*.ttf"\n'
            '    git add fonts/variable/HowsenLiuFangrun-VF.ttf\n'
        )
    os.makedirs(os.path.join(GH, 'fonts', 'ttc'), exist_ok=True)
    with open(os.path.join(GH, 'fonts', 'ttc', 'README.txt'), 'w', encoding='utf-8') as fh:
        fh.write(
            'HowsenLiuFangrun-TTC.ttc 约 120 MB，同样超过 GitHub 单文件上限，\n'
            '随 Release 附件分发；四个静态 TTF 已在 fonts/ttf/ 内，可用 fontTools 自行合并成 TTC。\n'
        )
    for f in ('HowsenLiuFangrun-VF.woff2', 'HowsenLiuFangrun-VF-subset.woff2',
              'HowsenLiuFangrun-VF-demo.woff2'):
        cp(os.path.join(BUILD, 'webfonts', f), os.path.join(GH, 'fonts', 'webfonts', f))

    # 母版 TTF 每个约 30 MB，8 个共约 240 MB，不进仓库；改为保留 designspace + 重建说明
    os.makedirs(os.path.join(GH, 'sources', 'masters'), exist_ok=True)
    with open(os.path.join(GH, 'sources', 'masters', 'README.txt'), 'w', encoding='utf-8') as fh:
        fh.write(
            '母版不随仓库分发（8 个 × 30 MB）。\n'
            '需要重建时，在装有 fontTools / skia-pathops / ufo2ft 的环境里执行：\n\n'
            '    python scripts/01_build_masters.py      # 由 Noto Sans SC VF 取 100/400/500/700 四实例，\n'
            '                                            # 统一圆角，派生 wdth75 / wdth105 / opsz12 / opsz72\n'
            '    python scripts/02_build_vf.py           # 生成 HowsenLiuFangrun-VF.ttf\n'
            '    python scripts/03_instances.py          # 静态 TTF + TTC + WOFF2\n'
            '    python scripts/05_qa.py                 # 插值兼容性报告\n\n'
            '母版文件名：HowsenLiuFangrun-{Light,Regular,Medium,Bold,Cond75,Exp105,Opt12,Opt72}-master.ttf\n'
            '依赖的唯一外部源字体：C:\\Windows\\Fonts\\NotoSansSC-VF.ttf（Noto Sans SC，SIL OFL 1.1）。\n'
        )
    cp(os.path.join(BUILD, 'HowsenLiuFangrun.designspace'),
       os.path.join(GH, 'sources', 'HowsenLiuFangrun.designspace'))
    cp(os.path.join(OLD, 'charset_all.csv'), os.path.join(GH, 'sources', 'charset', 'charset_all.csv'))
    cp(os.path.join(OLD, 'webfont-subset.txt'), os.path.join(GH, 'sources', 'charset', 'webfont-subset.txt'))

    SHIPPED = {'vf_lib.py', '01_build_masters.py', '02_build_vf.py', '03_instances.py',
               '04_specimens.py', '05_qa.py', '06_package.py',
               '14_fix_fvar_names.py', '17_rebuild_web.py'}
    for f in os.listdir(SCRIPTS):
        if f in SHIPPED:
            cp(os.path.join(SCRIPTS, f), os.path.join(GH, 'scripts', f))

    cp_tree(os.path.join(BUILD, 'specimen'), os.path.join(GH, 'specimen'))
    cp(os.path.join(BUILD, 'QA-插值兼容性报告.md'), os.path.join(GH, 'qa', 'QA-插值兼容性报告.md'))

    # ---------------- 2 网页部署
    os.makedirs(SITE, exist_ok=True)
    for f in ('HowsenLiuFangrun-VF.woff2', 'HowsenLiuFangrun-VF-subset.woff2',
              'HowsenLiuFangrun-VF-demo.woff2'):
        cp(os.path.join(BUILD, 'webfonts', f), os.path.join(SITE, 'site', 'fonts', 'webfonts', f))

    # ---------------- 3 字体下载
    cp(os.path.join(BUILD, 'HowsenLiuFangrun-VF.ttf'),
       os.path.join(DL, 'VF', 'HowsenLiuFangrun-VF.ttf'))
    cp(os.path.join(BUILD, 'webfonts', 'HowsenLiuFangrun-VF.woff2'),
       os.path.join(DL, 'VF', 'HowsenLiuFangrun-VF.woff2'))
    for style in STATIC:
        cp(os.path.join(BUILD, 'static', f'HowsenLiuFangrun-{style}.ttf'),
           os.path.join(DL, '静态TTF', f'HowsenLiuFangrun-{style}.ttf'))
    cp(os.path.join(BUILD, 'static', 'HowsenLiuFangrun-TTC.ttc'),
       os.path.join(DL, 'TTC', 'HowsenLiuFangrun-TTC.ttc'))
    for f in ('HowsenLiuFangrun-VF.woff2', 'HowsenLiuFangrun-VF-subset.woff2',
              'HowsenLiuFangrun-VF-demo.woff2'):
        cp(os.path.join(BUILD, 'webfonts', f), os.path.join(DL, 'WOFF2网页字体', f))

    shutil.copy2(os.path.join(GH, 'LICENSE'), os.path.join(DL, 'LICENSE-OFL-1.1.txt'))

    mkzip(os.path.join(DL, 'HowsenLiuFangrun-VF.zip'), [
        (os.path.join(DL, 'VF', 'HowsenLiuFangrun-VF.ttf'), 'HowsenLiuFangrun-VF.ttf'),
        (os.path.join(DL, 'VF', 'HowsenLiuFangrun-VF.woff2'), 'HowsenLiuFangrun-VF.woff2'),
        (os.path.join(GH, 'LICENSE'), 'LICENSE-OFL-1.1.txt'),
        (os.path.join(GH, 'FONTLOG.txt'), 'FONTLOG.txt'),
    ])
    mkzip(os.path.join(DL, 'HowsenLiuFangrun-Static-TTF.zip'),
          [(os.path.join(DL, '静态TTF', f'HowsenLiuFangrun-{s}.ttf'),
            f'HowsenLiuFangrun-{s}.ttf') for s in STATIC] +
          [(os.path.join(GH, 'LICENSE'), 'LICENSE-OFL-1.1.txt')])
    mkzip(os.path.join(DL, 'HowsenLiuFangrun-TTC.zip'), [
        (os.path.join(DL, 'TTC', 'HowsenLiuFangrun-TTC.ttc'), 'HowsenLiuFangrun-TTC.ttc'),
        (os.path.join(GH, 'LICENSE'), 'LICENSE-OFL-1.1.txt'),
    ])
    mkzip(os.path.join(DL, 'HowsenLiuFangrun-WOFF2.zip'), [
        (os.path.join(DL, 'WOFF2网页字体', 'HowsenLiuFangrun-VF.woff2'), 'HowsenLiuFangrun-VF.woff2'),
        (os.path.join(DL, 'WOFF2网页字体', 'HowsenLiuFangrun-VF-subset.woff2'),
         'HowsenLiuFangrun-VF-subset.woff2'),
        (os.path.join(DL, 'WOFF2网页字体', 'HowsenLiuFangrun-VF-demo.woff2'),
         'HowsenLiuFangrun-VF-demo.woff2'),
        (os.path.join(GH, 'LICENSE'), 'LICENSE-OFL-1.1.txt'),
    ])

    # ---------------- 4 样张预览
    cp_tree(os.path.join(BUILD, 'specimen'), os.path.join(PREVIEW, '样张'))

    print('完成：', PKG)


if __name__ == '__main__':
    main()
