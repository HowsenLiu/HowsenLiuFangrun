"""02  用 8 个同源母版构建三轴可变字体 HowsenLiuFangrun-VF.ttf

轴：wght 100-700 (默认 400) / wdth 75-105 (默认 100) / opsz 12-72 (默认 16)
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fontTools.designspaceLib import (AxisDescriptor, DesignSpaceDocument,
                                      InstanceDescriptor, SourceDescriptor)
from fontTools.ttLib import TTFont, newTable
from fontTools.varLib import build as varlib_build

import vf_lib  # noqa: F401  (确保脚本目录可用)

FAMILY_EN = 'HowsenLiu Fangrun'
FAMILY_ZH = '柳皓升方润黑体'
PS_NAME = 'HowsenLiuFangrun-VF'
VERSION = 'Version 2.000'

COPYRIGHT = ('Copyright © 2026 柳皓升 (Howsen Liu). '
             'Glyph skeleton based on Noto Sans CJK SC / Noto Sans SC, Copyright 2014-2021 Adobe '
             '(http://www.adobe.com/), licensed under the SIL Open Font License 1.1. '
             'Noto is a trademark of Google Inc.')
COPYRIGHT_ZH = ('版权 © 2026 柳皓升 (Howsen Liu)。'
                '字形骨架基于 Noto Sans CJK SC / Noto Sans SC（版权归 Adobe 所有，'
                'SIL Open Font License 1.1 授权），Noto 是 Google Inc. 的商标。')

MASTERS = [
    ('Light', 'HowsenLiuFangrun-Light-master.ttf', dict(wght=100, wdth=100, opsz=16), 100),
    ('Regular', 'HowsenLiuFangrun-Regular-master.ttf', dict(wght=400, wdth=100, opsz=16), 400),
    ('Medium', 'HowsenLiuFangrun-Medium-master.ttf', dict(wght=500, wdth=100, opsz=16), 500),
    ('Bold', 'HowsenLiuFangrun-Bold-master.ttf', dict(wght=700, wdth=100, opsz=16), 700),
    ('Condensed', 'HowsenLiuFangrun-Cond75-master.ttf', dict(wght=400, wdth=75, opsz=16), 400),
    ('Expanded', 'HowsenLiuFangrun-Exp105-master.ttf', dict(wght=400, wdth=105, opsz=16), 400),
    ('Caption', 'HowsenLiuFangrun-Opt12-master.ttf', dict(wght=400, wdth=100, opsz=12), 400),
    ('Display', 'HowsenLiuFangrun-Opt72-master.ttf', dict(wght=400, wdth=100, opsz=72), 400),
]

AXES = [
    dict(tag='wght', name='Weight', min=100, default=400, max=700,
         labels=[(100, 'Light'), (400, 'Regular'), (500, 'Medium'), (700, 'Bold')]),
    dict(tag='wdth', name='Width', min=75, default=100, max=105,
         labels=[(75, 'Condensed'), (100, 'Normal'), (105, 'Expanded')]),
    dict(tag='opsz', name='Optical Size', min=12, default=16, max=72,
         labels=[(12, 'Caption'), (16, 'Text'), (72, 'Display')]),
]

INSTANCES = [
    ('Light', 'Light', dict(wght=100, wdth=100, opsz=16), 'HowsenLiuFangrun-Light'),
    ('Regular', 'Regular', dict(wght=400, wdth=100, opsz=16), 'HowsenLiuFangrun-Regular'),
    ('Medium', 'Medium', dict(wght=500, wdth=100, opsz=16), 'HowsenLiuFangrun-Medium'),
    ('Bold', 'Bold', dict(wght=700, wdth=100, opsz=16), 'HowsenLiuFangrun-Bold'),
    ('Condensed', 'Condensed', dict(wght=400, wdth=75, opsz=16), 'HowsenLiuFangrun-Condensed'),
    ('Expanded', 'Expanded', dict(wght=400, wdth=105, opsz=16), 'HowsenLiuFangrun-Expanded'),
    ('Caption', 'Caption', dict(wght=400, wdth=100, opsz=12), 'HowsenLiuFangrun-Caption'),
    ('Display', 'Display Bold', dict(wght=700, wdth=100, opsz=72), 'HowsenLiuFangrun-DisplayBold'),
]


def make_ds(master_dir):
    ds = DesignSpaceDocument()
    for a in AXES:
        ax = AxisDescriptor()
        ax.tag = a['tag']
        ax.name = a['tag']
        ax.minimum = a['min']
        ax.default = a['default']
        ax.maximum = a['max']
        ax.map_forward = ax.map_backward = lambda x: x
        ds.addAxis(ax)

    dflt = None
    for style, fn, loc, wclass in MASTERS:
        s = SourceDescriptor()
        s.filename = os.path.join(master_dir, fn)
        s.path = os.path.abspath(s.filename)
        s.name = style
        s.familyName = FAMILY_EN
        s.styleName = style
        s.location = loc
        if loc == dict(wght=400, wdth=100, opsz=16):
            s.copyInfo = True
            s.copyLib = True
            s.copyFeatures = True
            s.copyGroups = True
            dflt = s
        ds.addSource(s)
    ds.findDefault()

    for style, sub, loc, ps in INSTANCES:
        i = InstanceDescriptor()
        i.familyName = FAMILY_EN
        i.styleName = sub
        i.postScriptFontName = ps
        i.location = loc
        i.name = style
        ds.addInstance(i)
    return ds


def _label(tag, value, name, default):
    from fontTools.designspaceLib import AxisLabelDescriptor
    lab = AxisLabelDescriptor(name=name, userValue=value, elidable=(value == default),
                              olderSibling=False)
    lab.userMinimum = value
    lab.userMaximum = value
    lab.linkedUserValue = None
    return lab


def set_names(font):
    recs = []
    def add(nid, en, zh=None):
        recs.append((3, 1, 0x409, nid, en))
        if zh:
            recs.append((3, 1, 0x804, nid, zh))

    add(0, COPYRIGHT, COPYRIGHT_ZH)
    add(1, FAMILY_EN, FAMILY_ZH)
    add(2, 'Regular', '常规')
    add(3, f'HLFR: {FAMILY_EN} Variable {VERSION}: 2026')
    add(4, f'{FAMILY_EN} Variable', f'{FAMILY_ZH} 可变字体')
    add(5, VERSION)
    add(6, PS_NAME)
    add(7, '柳皓升® · Noto is a trademark of Google Inc.')
    add(8, '柳皓升 (Howsen Liu)')
    add(9, '柳皓升 (Howsen Liu)。原字形骨架设计：Ryoko NISHIZUKA、Paul D. Hunt、'
           'Sandoll Communications（Noto Sans CJK）。')
    add(10, '柳皓升方润黑体 可变字体：三轴（字重 / 字宽 / 光学尺寸），32,000+ 字符，'
            'SIL OFL 1.1 授权，可免费商用。')
    add(13, 'This Font Software is licensed under the SIL Open Font License, Version 1.1. '
            'Available with a FAQ at: https://openfontlicense.org. '
            'Original skeleton: Noto Sans CJK SC, Copyright 2014-2021 Adobe, SIL OFL 1.1.',
        '本字体依据 SIL Open Font License 1.1 授权发布，可免费商用、修改与再分发；'
        '衍生字体须沿用 OFL 1.1。字形骨架基于 Noto Sans CJK SC（版权归 Adobe，OFL 1.1）。')
    add(14, 'https://openfontlicense.org')
    add(16, FAMILY_EN, FAMILY_ZH)
    add(17, 'Variable', '可变')
    add(25, 'HowsenLiuFangrun', 'HowsenLiuFangrun')

    name = newTable('name')
    name.names = []
    for pid, eid, lid, nid, val in recs:
        name.setName(val, nid, pid, eid, lid)
    font['name'] = name


def build_stat(font):
    try:
        from fontTools.otlLib.builder import buildStatTable
    except Exception:
        return
    axes = []
    for a in AXES:
        axes.append(dict(tag=a['tag'], name=a['name'],
                         ordering=len(axes),
                         values=[dict(value=v, name=n, flags=0x2 if v == a['default'] else 0)
                                 for v, n in a['labels']]))
    try:
        buildStatTable(font, axes)
    except Exception as exc:
        print('STAT 生成失败:', exc)


def fix_fvar_names(font):
    """fvar 的轴名与命名实例名对齐 STAT 已建的 nameID，避免显示为空或错位。"""
    axis_ids = {'wght': 256, 'wdth': 261, 'opsz': 265}
    for a in font['fvar'].axes:
        a.axisNameID = axis_ids[a.axisTag]
    inst = [('Light', '细体'), ('Regular', '常规'), ('Medium', '中粗'), ('Bold', '粗体'),
            ('Condensed', '窄体'), ('Expanded', '宽体'), ('Caption', '小字'),
            ('Display Bold', '大标题粗')]
    nm = font['name']
    for i, (en, zh) in enumerate(inst):
        nid = 269 + i * 2
        nm.setName(en, nid, 3, 1, 0x409)
        nm.setName(zh, nid, 3, 1, 0x804)
        font['fvar'].instances[i].subfamilyNameID = nid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--masters', default=os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'build', 'masters'))
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    out = a.out or os.path.join(os.path.dirname(a.masters), 'HowsenLiuFangrun-VF.ttf')

    ds = make_ds(a.masters)
    ds.write(os.path.join(a.masters, '..', 'HowsenLiuFangrun.designspace'))
    print('· designspace 就绪，开始构建 gvar …', flush=True)
    res = varlib_build(ds)
    vf = res[0]
    set_names(vf)
    build_stat(vf)
    os2 = vf['OS/2']
    os2.usWeightClass = 400
    os2.usWidthClass = 5
    os2.sTypoAscender = 1000
    os2.sTypoDescender = -250
    os2.sTypoLineGap = 0
    os2.usWinAscent = 1160
    os2.usWinDescent = 288
    os2.sxHeight = 536
    os2.sCapHeight = 733
    os2.achVendID = 'HLFR'
    os2.fsType = 0
    vf['head'].fontRevision = 2.0
    fix_fvar_names(vf)
    vf.save(out)
    print(f'· 已生成 {out} ({os.path.getsize(out) / 1e6:.1f} MB)')
    f = TTFont(out, lazy=True)
    print('  axes:', [(a.axisTag, a.minValue, a.defaultValue, a.maxValue) for a in f['fvar'].axes])
    print('  instances:', len(f['fvar'].instances), ' glyphs:', f['maxp'].numGlyphs)


if __name__ == '__main__':
    main()
