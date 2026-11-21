"""03  导出静态实例、TTC 集合包、WOFF2（全量 + GB2312 子集）

产物：
  build/static/HowsenLiuFangrun-{Light,Regular,Medium,Bold}.ttf
  build/static/HowsenLiuFangrun-TTC.ttc
  build/webfonts/HowsenLiuFangrun-VF.woff2
  build/webfonts/HowsenLiuFangrun-VF-subset.woff2
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fontTools.ttLib import TTCollection, TTFont, newTable
from fontTools.varLib.instancer import instantiateVariableFont

FAMILY_EN = 'HowsenLiu Fangrun'
FAMILY_ZH = '柳皓升方润黑体'
PS_PREFIX = 'HowsenLiuFangrun'
VERSION = 'Version 2.000'
VENDOR = 'HLFR'

STYLES = [
    ('Light', 100, '细体'),
    ('Regular', 400, '常规'),
    ('Medium', 500, '中粗'),
    ('Bold', 700, '粗体'),
]

COPYRIGHT = ('Copyright © 2026 柳皓升 (Howsen Liu). '
             'Glyph skeleton based on Noto Sans CJK SC / Noto Sans SC and Noto Sans KR, '
             'Copyright 2014-2021 Adobe (http://www.adobe.com/), licensed under the SIL Open '
             'Font License 1.1. Noto is a trademark of Google Inc.')
COPYRIGHT_ZH = ('版权 © 2026 柳皓升 (Howsen Liu)。字形骨架基于 Noto Sans CJK SC / Noto Sans SC '
                '与 Noto Sans KR（版权归 Adobe 所有，SIL OFL 1.1 授权）。Noto 是 Google Inc. 的商标。')
DESCRIPTION = ('柳皓升方润黑体：方中带圆的三轴可变字体（字重/字宽/光学尺寸），含中文、日文、谚文，'
               'SIL OFL 1.1 授权，可免费商用。')
LICENSE_EN = ('This Font Software is licensed under the SIL Open Font License, Version 1.1. '
              'Available with a FAQ at: https://openfontlicense.org. '
              'Original skeleton: Noto Sans CJK SC / Noto Sans KR, Copyright 2014-2021 Adobe, SIL OFL 1.1.')
LICENSE_ZH = ('本字体依据 SIL Open Font License 1.1 授权发布，可免费商用、修改与再分发；'
              '衍生字体须沿用 OFL 1.1。字形骨架基于 Noto Sans CJK SC / Noto Sans KR。')


def set_names(font, style, weight, zh):
    def add(nid, en, zh_s=None):
        recs.append((3, 1, 0x409, nid, en))
        if zh_s:
            recs.append((3, 1, 0x804, nid, zh_s))

    recs = []
    full_en = f'{FAMILY_EN} {style}'
    full_zh = f'{FAMILY_ZH} {zh}'
    add(0, COPYRIGHT, COPYRIGHT_ZH)
    add(1, FAMILY_EN, FAMILY_ZH)
    add(2, style, zh)
    add(3, f'{VENDOR}: {full_en} {VERSION}: 2026')
    add(4, full_en, full_zh)
    add(5, VERSION)
    add(6, f'{PS_PREFIX}-{style}')
    add(7, '柳皓升® · Noto is a trademark of Google Inc.')
    add(8, '柳皓升 (Howsen Liu)')
    add(9, '柳皓升 (Howsen Liu)。原字形骨架设计：Ryoko NISHIZUKA、Paul D. Hunt、'
           'Sandoll Communications（Noto Sans CJK SC / Noto Sans KR）。')
    add(10, DESCRIPTION, DESCRIPTION)
    add(13, LICENSE_EN, LICENSE_ZH)
    add(14, 'https://openfontlicense.org')
    add(16, FAMILY_EN, FAMILY_ZH)
    add(17, style, zh)

    name = newTable('name')
    name.names = []
    for pid, eid, lid, nid, val in recs:
        name.setName(val, nid, pid, eid, lid)
    font['name'] = name

    os2 = font['OS/2']
    os2.version = 4
    os2.usWeightClass = weight
    os2.usWidthClass = 5
    os2.sTypoAscender = 1000
    os2.sTypoDescender = -250
    os2.sTypoLineGap = 0
    os2.usWinAscent = 1160
    os2.usWinDescent = 288
    os2.sxHeight = 536
    os2.sCapHeight = 733
    os2.achVendID = VENDOR
    os2.fsType = 0
    os2.fsSelection &= ~0b1000001
    if weight == 400:
        os2.fsSelection |= 0b1000000
    if weight >= 700:
        os2.fsSelection |= 0b100000
    os2.fsSelection |= 1 << 7
    font['head'].fontRevision = 2.0
    font['head'].macStyle = 1 if weight >= 700 else 0
    hhea = font['hhea']
    hhea.ascent = 1000
    hhea.descent = -250
    hhea.lineGap = 0
    for tag in ('STAT', 'fvar', 'gvar', 'avar', 'HVAR', 'MVAR'):
        if tag in font:
            del font[tag]
    font['post'].formatType = 2.0
    font['post'].glyphOrder = None
    font['post'].extraNames = []
    font['post'].mapping = {}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vf_path = os.path.join(root, 'build', 'HowsenLiuFangrun-VF.ttf')
    out_static = os.path.join(root, 'build', 'static')
    out_web = os.path.join(root, 'build', 'webfonts')
    os.makedirs(out_static, exist_ok=True)
    os.makedirs(out_web, exist_ok=True)

    paths = []
    for style, weight, zh in STYLES:
        f = TTFont(vf_path)
        inst = instantiateVariableFont(f, {'wght': weight, 'wdth': 100, 'opsz': 16},
                                       inplace=False, updateFontNames=False)
        set_names(inst, style, weight, zh)
        p = os.path.join(out_static, f'{PS_PREFIX}-{style}.ttf')
        inst.save(p)
        paths.append(p)
        print(f'  静态 {style}: {os.path.getsize(p) / 1e6:.1f} MB')

    ttc_path = os.path.join(out_static, f'{PS_PREFIX}-TTC.ttc')
    ttc = TTCollection()
    ttc.fonts = [TTFont(p) for p in paths]
    ttc.save(ttc_path, shareTables=True)
    print(f'  TTC: {os.path.getsize(ttc_path) / 1e6:.1f} MB')

    # WOFF2 全量
    fw = TTFont(vf_path)
    fw.flavor = 'woff2'
    wpath = os.path.join(out_web, f'{PS_PREFIX}-VF.woff2')
    fw.save(wpath)
    print(f'  WOFF2 全量: {os.path.getsize(wpath) / 1e6:.2f} MB')

    # WOFF2 GB2312 子集
    from fontTools import subset as ftsub
    subset_txt = (r'C:\Users\12784\Desktop\字体\柳皓升方润黑体-发布包\发布包'
                  r'\1_GitHub仓库上传\sources\charset\webfont-subset.txt')
    text = open(subset_txt, encoding='utf-8').read()
    opts = ftsub.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = ['*']
    opts.drop_tables = []
    opts.desubroutinize = True
    font = TTFont(vf_path)
    subsetter = ftsub.Subsetter(options=opts)
    subsetter.populate(text=text)
    subsetter.subset(font)
    spath = os.path.join(out_web, f'{PS_PREFIX}-VF-subset.woff2')
    font.save(spath)
    print(f'  WOFF2 子集: {os.path.getsize(spath) / 1e6:.2f} MB '
          f'({font["maxp"].numGlyphs} glyphs)')


if __name__ == '__main__':
    main()
