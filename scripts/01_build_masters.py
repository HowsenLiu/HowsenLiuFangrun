"""01  从 Noto Sans SC 可变字体生成 8 个结构同源的母版 TTF

母版（designspace 顶点）：
  wght 100 / 400 / 500 / 700  ← 原生实例，骨架同源
  wdth 75 / 105               ← Regular 上的横向缩放母版
  opsz 12 / 72                ← 笔画补偿 + 字面缩放母版

所有母版的每个字符：轮廓数、点数、点序、on/off 标记完全一致。
"""
from __future__ import annotations

import argparse
import os
import sys
import time
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fontTools.ttLib import TTFont, newTable
from fontTools.varLib.instancer import instantiateVariableFont

import vf_lib as L

SRC_VF = r"C:\Windows\Fonts\NotoSansSC-VF.ttf"
OLD_REGULAR = (r"C:\Users\12784\Desktop\字体\柳皓升方润黑体-发布包\发布包"
               r"\1_GitHub仓库上传\fonts\ttf\HowsenLiuFangrun-Regular.ttf")
CHARSET_CSV = (r"C:\Users\12784\Desktop\字体\柳皓升方润黑体-发布包\发布包"
               r"\1_GitHub仓库上传\sources\charset\charset_all.csv")

WEIGHTS = [('Light', 100, 100), ('Regular', 400, 400), ('Medium', 500, 500), ('Bold', 700, 700)]

# 派生母版参数
WDTH = {'Condensed': 0.75, 'Expanded': 1.05}
OPSZ_SMALL = dict(w=0.41, scale=1.02)     # opsz 12：向 Medium 借 41% 笔画，字面放大 2%
OPSZ_BIG = dict(w=0.29, scale=1.00)       # opsz 72：向 Light 借 29% 笔画，细节收细
SYN_OFFSET = {'Light': -28.0, 'Medium': 22.0, 'Bold': 50.0}   # 补字合成用


def log(msg):
    print(msg, flush=True)


def structure(contours):
    return [(len(c), tuple(bool(p[2]) for p in c)) for c in contours]


def build(limit=None, out_dir='build/masters', add_missing=True):
    t0 = time.time()
    os.makedirs(out_dir, exist_ok=True)

    log('· 载入可变字体并实例化四个字重 …')
    inst = {}
    for style, wght, _ in WEIGHTS:
        f = TTFont(SRC_VF)
        v = instantiateVariableFont(f, {'wght': wght}, inplace=False, optimize=False)
        inst[style] = v
        log(f'  {style}: {len(v.getGlyphOrder())} glyphs')

    # 模板（供 8 个母版复用表结构）
    tmpl_path = os.path.join(out_dir, '..', 'template-400.ttf')
    inst['Regular'].save(tmpl_path)

    order = inst['Regular'].getGlyphOrder()
    if limit:
        order = order[:limit]

    glyf_tables = {k: newTable('glyf') for k in
                   ('wght100', 'wght400', 'wght500', 'wght700', 'wdth75', 'wdth105', 'opsz12', 'opsz72')}
    for k, g in glyf_tables.items():
        g.glyphs = {}
        g.glyphOrder = inst['Regular'].getGlyphOrder()

    metrics = {k: {} for k in glyf_tables}
    stats = dict(glyphs=0, repaired=0, skipped=0)
    t_parse = time.time()

    for gi, name in enumerate(order):
        gs = []
        for style, _, _ in WEIGHTS:
            g = inst[style]['glyf'][name]
            gs.append(g)
        contours = [L.glyph_to_contours(g) for g in gs]
        if any(len(c) != len(contours[1]) for c in contours):
            stats['skipped'] += 1
            continue
        if contours[0] and structure(contours[0]) != structure(contours[1]):
            stats['skipped'] += 1
            if stats['skipped'] < 8:
                log(f'  结构不一致，跳过 {name}')
            continue

        segs = [[L.to_cubic(L.contour_to_segs(c)) for c in cs] for cs in contours]
        plans = [L.plan_contour(cs) for cs in segs[1]]      # Regular 上的圆角计划

        polys = []
        for wi in range(4):
            filled = []
            for ci, cs in enumerate(segs[wi]):
                filled.append(L.apply_fillet(cs, plans[ci]) if cs else cs)
            poly = L.contours_to_poly(filled)
            polys.append(poly)
            adv = inst[WEIGHTS[wi][0]]['hmtx'][name][0]
            keys = ('wght100', 'wght400', 'wght500', 'wght700')[wi]
            glyf_tables[keys].glyphs[name] = L.poly_to_glyph(poly)
            metrics[keys][name] = (adv, int(round(min(poly[0]))) if poly[0] else 0)

        # ---- 宽度轴母版（以 Regular 为基准横向缩放）
        reg_poly = polys[1]
        reg_adv = metrics['wght400'][name][0]
        for key, k in (('wdth75', WDTH['Condensed']), ('wdth105', WDTH['Expanded'])):
            p = L.poly_affine(reg_poly, k, 1.0)
            glyf_tables[key].glyphs[name] = L.poly_to_glyph(p)
            metrics[key][name] = (int(round(reg_adv * k)), int(round(min(p[0]))) if p[0] else 0)

        # ---- 光学尺寸轴母版
        med_poly = polys[2]
        light_poly = polys[0]
        p12 = L.poly_blend(reg_poly, med_poly, OPSZ_SMALL['w'],
                           OPSZ_SMALL['scale'], OPSZ_SMALL['scale'],
                           cx=reg_adv * 0.5, cy=380.0)
        glyf_tables['opsz12'].glyphs[name] = L.poly_to_glyph(p12)
        metrics['opsz12'][name] = (reg_adv, int(round(min(p12[0]))) if p12[0] else 0)

        p72 = L.poly_blend(reg_poly, light_poly, OPSZ_BIG['w'])
        glyf_tables['opsz72'].glyphs[name] = L.poly_to_glyph(p72)
        metrics['opsz72'][name] = (reg_adv, int(round(min(p72[0]))) if p72[0] else 0)

        stats['glyphs'] += 1
        if (gi + 1) % 2000 == 0:
            log(f'  {gi + 1}/{len(order)}  {time.time() - t_parse:.0f}s')

    log(f'· 主轮廓完成 {stats["glyphs"]} 字，跳过 {stats["skipped"]}，'
        f'用时 {time.time() - t_parse:.0f}s')

    # ---- 补字（ExtB / 兼容表 / 其他旧版有而新母版缺的字符）
    extra_cmap, extra_order = {}, []
    if add_missing and not limit:
        extra_cmap, extra_order = build_missing(glyf_tables, metrics, inst)

    glyph_order = inst['Regular'].getGlyphOrder()[:limit] + extra_order
    for k in glyf_tables:
        glyf_tables[k].glyphOrder = glyph_order

    # ---- 保存 8 个母版
    for key, style in (('wght100', 'Light'), ('wght400', 'Regular'),
                       ('wght500', 'Medium'), ('wght700', 'Bold'),
                       ('wdth75', 'Cond75'), ('wdth105', 'Exp105'),
                       ('opsz12', 'Opt12'), ('opsz72', 'Opt72')):
        f = TTFont(tmpl_path)
        # 必须先载入旧 loca / vmtx，否则 maxp 改号后旧表反序列化会按错长度截断
        _ = f['loca']
        _ = f['head']
        vmetrics = dict(f['vmtx'].metrics)
        _ = f['vhea']
        f['glyf'] = glyf_tables[key]
        f['loca'] = newTable('loca')
        hmtx = newTable('hmtx')
        hmtx.metrics = {n: metrics[key].get(n, (1000, 0)) for n in glyph_order}
        f['hmtx'] = hmtx
        f.setGlyphOrder(glyph_order)
        f['maxp'].numGlyphs = len(glyph_order)

        # 竖排度量：沿用模板每字 tsb，补字按 vOriginY=880 计算
        vmtx = newTable('vmtx')
        vmtx.metrics = {}
        for n in glyph_order:
            if n in vmetrics:
                vmtx.metrics[n] = vmetrics[n]
            else:
                g = glyf_tables[key].glyphs[n]
                ymax = max((y for x, y in g.coordinates), default=0) if g.numberOfContours else 0
                vmtx.metrics[n] = (1000, int(round(880 - ymax)))
        f['vmtx'] = vmtx
        adv = [vmtx.metrics[n][0] for n in glyph_order]
        last = adv[-1]
        nlong = len(adv)
        while nlong > 1 and adv[nlong - 2] == last:
            nlong -= 1
        vhea = f['vhea']
        vhea.numberOfVMetrics = max(1, nlong)
        vhea.advanceHeightMax = max(adv)
        if 'post' in f:
            f['post'].formatType = 2.0
            f['post'].glyphOrder = None
            f['post'].extraNames = []
            f['post'].mapping = {}
        # cmap：补字 + 兼容区别名
        if extra_cmap:
            for t in f['cmap'].tables:
                if t.format == 4:
                    for cp, gn in extra_cmap.items():
                        if cp <= 0xFFFF:
                            t.cmap[cp] = gn
                elif t.format == 12:
                    for cp, gn in extra_cmap.items():
                        t.cmap[cp] = gn
        path = os.path.join(out_dir, f'HowsenLiuFangrun-{style}-master.ttf')
        f.save(path)
        log(f'  母版 {style}: {path} ({os.path.getsize(path) / 1e6:.1f} MB)')

    log(f'总用时 {time.time() - t0:.0f}s')


def build_missing(glyf_tables, metrics, inst):
    """旧版有、新母版缺的字符：兼容区做别名，其余从旧 Regular 轮廓按点位移合成四字重。"""
    import csv
    old = TTFont(OLD_REGULAR)
    old_cmap = old.getBestCmap()
    old_glyf = old['glyf']
    new_cmap = set(inst['Regular'].getBestCmap())
    cmap_dict = inst['Regular'].getBestCmap()

    cps = set()
    with open(CHARSET_CSV, encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh):
            cps.add(int(r['decimal']))

    alias, synth = {}, []
    for cp in sorted(cps - new_cmap):
        d = unicodedata.decomposition(chr(cp)).split()
        if len(d) == 1 and d[0]:
            try:
                base = int(d[0], 16)
            except ValueError:
                base = -1
            if base in new_cmap:
                alias[cp] = cmap_dict[base]
                continue
        synth.append(cp)

    extra_cmap = dict(alias)
    extra_order = []
    synth_ok = 0
    for cp in synth:
        gname = old_cmap.get(cp)
        if gname is None:
            continue
        name = f'uni{cp:04X}' if cp <= 0xFFFF else f'u{cp:05X}'
        try:
            contours = L.glyph_to_contours(old_glyf[gname])
            if not contours:
                continue
            segs = [L.to_cubic(L.contour_to_segs(c)) for c in contours]
            poly = L.contours_to_poly([[L.c_to_q(s) if s[0] == 'C' else s for s in cs]
                                       for cs in segs])
        except Exception as exc:
            print('  补字失败', hex(cp), exc)
            continue
        if not poly[0]:
            continue
        adv = old['hmtx'][gname][0]
        for key, off in (('wght400', 0.0), ('wght100', SYN_OFFSET['Light']),
                         ('wght500', SYN_OFFSET['Medium']), ('wght700', SYN_OFFSET['Bold'])):
            p = L.offset_poly(poly, off) if off else poly
            glyf_tables[key].glyphs[name] = L.poly_to_glyph(p)
            metrics[key][name] = (adv, int(round(min(p[0]))) if p[0] else 0)
        for key, k in (('wdth75', WDTH['Condensed']), ('wdth105', WDTH['Expanded'])):
            p = L.poly_affine(poly, k, 1.0)
            glyf_tables[key].glyphs[name] = L.poly_to_glyph(p)
            metrics[key][name] = (int(round(adv * k)), int(round(min(p[0]))) if p[0] else 0)
        for key, t, sc in (('opsz12', OPSZ_SMALL['w'], OPSZ_SMALL['scale']),
                           ('opsz72', OPSZ_BIG['w'], 1.0)):
            base = L.offset_poly(poly, SYN_OFFSET['Medium'] * t) if t else poly
            p = L.poly_affine(base, sc, sc, adv * 0.5, 380.0)
            glyf_tables[key].glyphs[name] = L.poly_to_glyph(p)
            metrics[key][name] = (adv, int(round(min(p[0]))) if p[0] else 0)
        extra_cmap[cp] = name
        extra_order.append(name)
        synth_ok += 1

    log(f'· 补字：别名 {len(alias)}，合成 {synth_ok}（共 {len(cps - new_cmap)}）')
    return extra_cmap, extra_order


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'build', 'masters'))
    ap.add_argument('--no-missing', action='store_true')
    a = ap.parse_args()
    build(limit=a.limit, out_dir=a.out, add_missing=not a.no_missing)

