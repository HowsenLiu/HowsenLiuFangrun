"""HowsenLiu Fangrun VF 核心几何库

设计原则：
1) 所有母版共享同一套轮廓结构（contour 数、点数、点序、on/off 标记完全一致）
2) 圆角计划只在 Regular 上计算一次，其他母版按同一份计划（同一 t、同一弧段数）套用
3) 字重来自 Noto Sans SC 可变字体原生实例（不是偏移生成），因此骨架天然同源
4) 宽度轴、光学尺寸轴只在同一结构上做仿射/加权变换
"""
from __future__ import annotations

import math
from array import array

from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import Glyph, GlyphCoordinates
from fontTools.ttLib.tables.ttProgram import Program

EPS = 1e-6
SQUARENESS = 1.06         # 圆角方圆度（>1 角部更饱满）
RADIUS = 88.0             # 圆角半径（单位/1000 em）
MIN_TURN_DEG = 17.0       # 小于此转角不做圆角
MAX_TRIM_RATIO = 2.0      # 切点距离上限 = 2R
ARC_DIV = math.pi / 4.0   # 每段圆弧的最大张角（45°），决定弧段数量


# ---------------------------------------------------------------- 向量工具
def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def vmul(a, k):
    return (a[0] * k, a[1] * k)


def vlen(a):
    return math.hypot(a[0], a[1])


def vunit(a):
    l = math.hypot(a[0], a[1])
    return (a[0] / l, a[1] / l) if l > EPS else (0.0, 0.0)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


# ---------------------------------------------------------------- 母版轮廓 → 段
def glyph_to_contours(glyph):
    """glyf Glyph → [[(x, y, on), ...], ...]"""
    if glyph.numberOfContours <= 0:
        return []
    coords = glyph.coordinates
    flags = glyph.flags
    contours = []
    start = 0
    for end in glyph.endPtsOfContours:
        pts = [(coords[i][0], coords[i][1], bool(flags[i] & 1)) for i in range(start, end + 1)]
        if len(pts) >= 2:
            contours.append(pts)
        start = end + 1
    return contours


def contour_to_segs(pts):
    """二次点列 → 段序列，段为 ('L', p0, p1) 或 ('Q', p0, c, p1)。"""
    n = len(pts)
    if n < 2:
        return []
    first_on = None
    for i, p in enumerate(pts):
        if p[2]:
            first_on = i
            break
    if first_on is None:
        # 全部是控制点：起点取首尾控制点中点的隐含点
        start = ((pts[-1][0] + pts[0][0]) * 0.5, (pts[-1][1] + pts[0][1]) * 0.5)
        seq = pts
        closed_all_off = True
    else:
        start = (pts[first_on][0], pts[first_on][1])
        seq = pts[first_on + 1:] + pts[:first_on]
        closed_all_off = False

    segs = []
    cur = start
    ctrl = None
    for p in seq:
        if p[2]:
            if ctrl is None:
                # 不退化解：每个 on-curve 点都产生一段，保证各母版段数完全一致
                segs.append(('L', cur, (p[0], p[1])))
            else:
                segs.append(('Q', cur, ctrl, (p[0], p[1])))
            cur = (p[0], p[1])
            ctrl = None
        else:
            cp = (p[0], p[1])
            if ctrl is not None:
                mid = ((ctrl[0] + cp[0]) * 0.5, (ctrl[1] + cp[1]) * 0.5)
                segs.append(('Q', cur, ctrl, mid))
                cur = mid
            ctrl = cp
    if ctrl is None:
        segs.append(('L', cur, start))
    else:
        segs.append(('Q', cur, ctrl, start))
    if closed_all_off and segs:
        pass
    return segs


def q_to_c(p0, c, p1):
    c1 = (p0[0] + 2.0 / 3.0 * (c[0] - p0[0]), p0[1] + 2.0 / 3.0 * (c[1] - p0[1]))
    c2 = (p1[0] + 2.0 / 3.0 * (c[0] - p1[0]), p1[1] + 2.0 / 3.0 * (c[1] - p1[1]))
    return ('C', p0, c1, c2, p1)


def to_cubic(segs):
    return [s if s[0] == 'L' else q_to_c(s[1], s[2], s[3]) for s in segs]


def c_to_q(seg):
    """三次段 → 单段二次（中点拟合），保证每段在每个母版上都只产生 1 个控制点。"""
    _, p0, c1, c2, p3 = seg
    q = ((3.0 * (c1[0] + c2[0]) - p0[0] - p3[0]) / 4.0,
         (3.0 * (c1[1] + c2[1]) - p0[1] - p3[1]) / 4.0)
    return ('Q', p0, q, p3)


# ---------------------------------------------------------------- 曲线基础量
def cubic_point(cp, t):
    mt = 1.0 - t
    a = mt * mt * mt
    b = 3 * mt * mt * t
    c = 3 * mt * t * t
    d = t * t * t
    return (a * cp[0][0] + b * cp[1][0] + c * cp[2][0] + d * cp[3][0],
            a * cp[0][1] + b * cp[1][1] + c * cp[2][1] + d * cp[3][1])


def cubic_split(cp, t):
    p0, p1, p2, p3 = cp
    q0 = vadd(p0, vmul(vsub(p1, p0), t))
    q1 = vadd(p1, vmul(vsub(p2, p1), t))
    q2 = vadd(p2, vmul(vsub(p3, p2), t))
    r0 = vadd(q0, vmul(vsub(q1, q0), t))
    r1 = vadd(q1, vmul(vsub(q2, q1), t))
    s = vadd(r0, vmul(vsub(r1, r0), t))
    return (p0, q0, r0, s), (s, r1, q2, p3)


def cubic_len(cp, n=12):
    pts = [cubic_point(cp, i / n) for i in range(n + 1)]
    return sum(dist(pts[i], pts[i + 1]) for i in range(n))


def _find_u(cp, target, from_start=True, n=16):
    pts = [cubic_point(cp, i / n) for i in range(n + 1)]
    acc = 0.0
    seq = range(n) if from_start else range(n, 0, -1)
    for i in seq:
        j = i + 1 if from_start else i - 1
        seg = dist(pts[i], pts[j])
        if acc + seg >= target:
            frac = (target - acc) / seg if seg > EPS else 0.0
            u = (i + frac) / n if from_start else (i - frac) / n
            return min(max(u, 0.0), 1.0)
        acc += seg
    return 1.0 if from_start else 0.0


def seg_end(s):
    return s[2] if s[0] == 'L' else s[3]


def seg_start(s):
    return s[1]


def seg_tan_end(s):
    if s[0] == 'L':
        return vunit(vsub(s[2], s[1]))
    _, p0, p1, p2, p3 = s
    d = vsub(p3, p2)
    if vlen(d) < EPS:
        d = vsub(p2, p1)
    if vlen(d) < EPS:
        d = vsub(p1, p0)
    return vunit(d)


def seg_tan_start(s):
    if s[0] == 'L':
        return vunit(vsub(s[2], s[1]))
    _, p0, p1, p2, p3 = s
    d = vsub(p1, p0)
    if vlen(d) < EPS:
        d = vsub(p2, p0)
    if vlen(d) < EPS:
        d = vsub(p3, p0)
    return vunit(d)


def seg_len(s):
    if s[0] == 'L':
        return dist(s[1], s[2])
    return cubic_len(s[1:])


def trim_seg_end(s, d):
    if d <= EPS:
        return s
    if s[0] == 'L':
        L = dist(s[1], s[2])
        if d >= L - EPS:
            return None
        u = vunit(vsub(s[2], s[1]))
        return ('L', s[1], (s[2][0] - u[0] * d, s[2][1] - u[1] * d))
    cp = s[1:]
    L = cubic_len(cp)
    if d >= L:
        return None
    u = _find_u(cp, d, from_start=False)
    left, _ = cubic_split(cp, u)
    return ('C', *left)


def trim_seg_start(s, d):
    if d <= EPS:
        return s
    if s[0] == 'L':
        L = dist(s[1], s[2])
        if d >= L - EPS:
            return None
        u = vunit(vsub(s[2], s[1]))
        return ('L', (s[1][0] + u[0] * d, s[1][1] + u[1] * d), s[2])
    cp = s[1:]
    L = cubic_len(cp)
    if d >= L:
        return None
    u = _find_u(cp, d, from_start=True)
    _, right = cubic_split(cp, u)
    return ('C', *right)


def point_at_end(s, d):
    q = trim_seg_end(s, d)
    return None if q is None else seg_end(q)


def point_at_start(s, d):
    q = trim_seg_start(s, d)
    return None if q is None else seg_start(q)


# ---------------------------------------------------------------- 圆角计划
def _line_intersection(A, dA, B, dB):
    den = dA[0] * dB[1] - dA[1] * dB[0]
    if abs(den) < 1e-9:
        return None
    t = ((B[0] - A[0]) * dB[1] - (B[1] - A[1]) * dB[0]) / den
    return (A[0] + dA[0] * t, A[1] + dA[1] * t)


def _arc_params(prev, nxt, t):
    """给定切点距离 t，返回 (A, B, C, r, sweep) 或 None。"""
    d_in = seg_tan_end(prev)
    d_out = seg_tan_start(nxt)
    A = point_at_end(prev, t)
    B = point_at_start(nxt, t)
    if A is None or B is None:
        return None
    C = _line_intersection(A, (-d_in[1], d_in[0]), B, (-d_out[1], d_out[0]))
    if C is None:
        return None
    r = dist(C, A)
    if r < 1.0 or abs(r - dist(C, B)) > 0.25 * r + 1.5:
        return None
    a0 = math.atan2(A[1] - C[1], A[0] - C[0])
    a1 = math.atan2(B[1] - C[1], B[0] - C[0])
    sweep = a1 - a0
    while sweep <= -math.pi:
        sweep += 2 * math.pi
    while sweep > math.pi:
        sweep -= 2 * math.pi
    return A, B, C, r, sweep


def plan_junction(prev, nxt, r=RADIUS, min_turn_deg=MIN_TURN_DEG, max_ratio=MAX_TRIM_RATIO):
    """在 Regular 上判定该交接点是否圆角，并记录绝对切距 t 与弧段数 K。"""
    d_in = seg_tan_end(prev)
    d_out = seg_tan_start(nxt)
    if vlen(d_in) < EPS or vlen(d_out) < EPS:
        return None
    cross = d_in[0] * d_out[1] - d_in[1] * d_out[0]
    dot = max(-1.0, min(1.0, d_in[0] * d_out[0] + d_in[1] * d_out[1]))
    turn = math.atan2(abs(cross), dot)
    if math.degrees(turn) < min_turn_deg:
        return None
    theta = math.pi - turn
    if theta < 1e-3:
        return None
    t_need = r / math.tan(theta / 2.0)
    t = min(t_need, 0.45 * seg_len(prev), 0.45 * seg_len(nxt), max_ratio * r)
    if t < 1.0:
        return None
    if t * math.tan(theta / 2.0) < 1.2:
        return None
    ap = _arc_params(prev, nxt, t)
    if ap is None:
        return None
    A, B, C, rad, sweep = ap
    if dist(A, seg_end(prev)) < 0.5 or dist(B, seg_start(nxt)) < 0.5:
        return None
    K = max(1, int(math.ceil(abs(sweep) / ARC_DIV - 1e-9)))
    return dict(t=t, K=K)


def plan_contour(segs):
    n = len(segs)
    plan = {}
    for i in range(n):
        j = (i + 1) % n
        p = plan_junction(segs[i], segs[j])
        if p is not None:
            plan[i] = p
    return plan


def _arc_quads(A, B, C, r, sweep, K):
    """把圆弧切成固定 K 段，每段用一个二次曲线表示（控制点=切线交点）。"""
    a0 = math.atan2(A[1] - C[1], A[0] - C[0])
    out = []
    steps = K
    cur_ang = a0
    cur_pt = A
    for k in range(steps):
        nxt_ang = a0 + sweep * (k + 1) / steps
        nxt_pt = (C[0] + r * math.cos(nxt_ang), C[1] + r * math.sin(nxt_ang))
        mid_ang = 0.5 * (cur_ang + nxt_ang)
        # 切线交点（squircle：手柄沿切线方向略加长）
        half = abs(nxt_ang - cur_ang) / 2.0
        k_len = SQUARENESS * math.tan(half) * r
        k_len = min(k_len, 0.95 * math.tan(half) * r + 1.0) if SQUARENESS > 1 else k_len
        ctrl = (C[0] + (r / max(math.cos(half), 1e-6)) * math.cos(mid_ang),
                C[1] + (r / max(math.cos(half), 1e-6)) * math.sin(mid_ang))
        # 方圆度 >1 时把控制点沿径向稍微外推，角部更饱满（近似 squircle）
        ctrl = (C[0] + (ctrl[0] - C[0]) * (1.0 + (SQUARENESS - 1.0) * 0.55),
                C[1] + (ctrl[1] - C[1]) * (1.0 + (SQUARENESS - 1.0) * 0.55))
        out.append(('Q', cur_pt, ctrl, nxt_pt))
        cur_pt = nxt_pt
        cur_ang = nxt_ang
    return out


def apply_fillet(segs, plan, r=RADIUS):
    """按计划（t、K 固定）在指定母版上真正生成圆角，结构必然一致。"""
    n = len(segs)
    plan = {i: p for i, p in plan.items() if 0 <= i < n}
    lengths = [seg_len(s) for s in segs]

    # 切距按该母版自身段长收敛，保证相邻段的修剪量一致
    ts = {}
    for i, p in plan.items():
        j = (i + 1) % n
        ts[i] = min(p['t'], 0.44 * lengths[i], 0.44 * lengths[j])
    for _ in range(3):
        for i in list(ts):
            j = (i + 1) % n
            if lengths[i] > EPS and ts[i] + ts.get((i - 1) % n, 0.0) > 0.9 * lengths[i]:
                ts[i] = max(0.5 * ts[i], 1.0)
            if lengths[j] > EPS and ts[i] + ts.get(j, 0.0) > 0.9 * lengths[j]:
                ts[i] = max(0.5 * ts[i], 1.0)

    out = []
    for i, s in enumerate(segs):
        t_in = ts.get((i - 1) % n, 0.0)
        t_out = ts.get(i, 0.0)
        a = trim_seg_start(s, t_in) if t_in > EPS else s
        if a is None:
            a = s
        b = trim_seg_end(a, t_out) if t_out > EPS else a
        if b is None:
            b = a
        out.append(b if b[0] == 'L' else c_to_q(b))
        if i in plan:
            K = plan[i]['K']
            t = ts[i]
            ap = _arc_params(segs[i], segs[(i + 1) % n], t)
            if ap is not None:
                A, B, C, rad, sweep = ap
                out.extend(_arc_quads(A, B, C, rad, sweep, K))
            else:
                # 退化：用 K 段直线（结构仍然是 K 个二次段）
                A = point_at_end(segs[i], t) or seg_end(segs[i])
                B = point_at_start(segs[(i + 1) % n], t) or seg_start(segs[(i + 1) % n])
                prev = A
                for k in range(K):
                    nxt = (A[0] + (B[0] - A[0]) * (k + 1) / K, A[1] + (B[1] - A[1]) * (k + 1) / K)
                    ctrl = ((prev[0] + nxt[0]) * 0.5, (prev[1] + nxt[1]) * 0.5)
                    out.append(('Q', prev, ctrl, nxt))
                    prev = nxt
    return out


# ---------------------------------------------------------------- 结构 → 点列
def segs_to_points(segs):
    """段序列（二次）→ (xs, ys, on_flags, contour_points) 点列；返回闭合轮廓点列。"""
    pts = []
    for s in segs:
        if s[0] == 'L':
            pts.append((s[2][0], s[2][1], 1))
        else:
            pts.append((s[2][0], s[2][1], 0))
            pts.append((s[3][0], s[3][1], 1))
    return pts


def contours_to_poly(contours_segs):
    """[[segs]] → (xs, ys, ons, ends)"""
    xs, ys, ons, ends = [], [], [], []
    for segs in contours_segs:
        if not segs:
            continue
        pts = [(segs[0][1][0], segs[0][1][1], 1)] + segs_to_points(segs)
        for x, y, on in pts:
            xs.append(x)
            ys.append(y)
            ons.append(on)
        ends.append(len(xs) - 1)
    return xs, ys, ons, ends


def poly_to_glyph(poly):
    xs, ys, ons, ends = poly
    g = Glyph()
    g.numberOfContours = len(ends)
    g.coordinates = GlyphCoordinates(list(zip(xs, ys)))
    g.flags = array('B', [1 if on else 0 for on in ons])
    g.endPtsOfContours = list(ends)
    g.program = Program()
    return g


def poly_transform(poly, fx, fy=None):
    xs, ys, ons, ends = poly
    if fy is None:
        return [fx(x, y) for x, y in zip(xs, ys)], ys, ons, ends
    return [fx(x, y) for x, y in zip(xs, ys)], [fy(x, y) for x, y in zip(xs, ys)], ons, ends


def poly_affine(poly, sx, sy=1.0, cx=0.0, cy=0.0, dx=0.0):
    """x' = cx + (x-cx)*sx + dx, y' = cy + (y-cy)*sy"""
    xs, ys, ons, ends = poly
    nxs = [cx + (x - cx) * sx + dx for x in xs]
    nys = [cy + (y - cy) * sy for y in ys]
    return nxs, nys, ons, ends


def poly_blend(a, b, t, extra_sx=1.0, extra_sy=1.0, cx=0.0, cy=0.0):
    """点对点加权（结构一致前提），再做字面缩放。"""
    nxs = []
    nys = []
    ax, ay, _, _ = a
    bx, by, _, _ = b
    for x0, y0, x1, y1 in zip(ax, ay, bx, by):
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        nxs.append(cx + (x - cx) * extra_sx)
        nys.append(cy + (y - cy) * extra_sy)
    return nxs, nys, a[2], a[3]


# ---------------------------------------------------------------- 点列 → 偏移（补字用）
def _area(xs, ys):
    s = 0.0
    n = len(xs)
    for i in range(n):
        j = (i + 1) % n
        s += xs[i] * ys[j] - xs[j] * ys[i]
    return s * 0.5


def offset_poly(poly, d, max_ratio=0.55):
    """结构保持的等距外扩（d>0 加粗）/内缩（d<0）。用于补字字重的合成。"""
    xs, ys, ons, ends = poly
    if abs(d) < 0.2:
        return list(xs), list(ys), ons, ends
    nxs = list(xs)
    nys = list(ys)
    start = 0
    for end in ends:
        idx = list(range(start, end + 1))
        start = end + 1
        cx = [xs[i] for i in idx]
        cy = [ys[i] for i in idx]
        ccw = _area(cx, cy) > 0
        m = len(idx)
        disp = [None] * m
        for k in range(m):
            p = idx[k]
            prev = idx[(k - 1) % m]
            nxt = idx[(k + 1) % m]
            e1 = vunit((xs[p] - xs[prev], ys[p] - ys[prev]))
            e2 = vunit((xs[nxt] - xs[p], ys[nxt] - ys[p]))
            if ccw:
                n1 = (e1[1], -e1[0])
                n2 = (e2[1], -e2[0])
            else:
                n1 = (-e1[1], e1[0])
                n2 = (-e2[1], e2[0])
            den = 1.0 + n1[0] * n2[0] + n1[1] * n2[1]
            if den < 0.35:
                n1 = vunit((n1[0] + n2[0], n1[1] + n2[1]))
                n2 = n1
                den = 1.0 + n1[0] * n2[0] + n1[1] * n2[1]
                if den < 0.05:
                    den = 1.0
            dx = d * (n1[0] + n2[0]) / den
            dy = d * (n1[1] + n2[1]) / den
            lim = max_ratio * min(dist((xs[p], ys[p]), (xs[prev], ys[prev])),
                                  dist((xs[p], ys[p]), (xs[nxt], ys[nxt])))
            ln = math.hypot(dx, dy)
            if lim > 1e-6 and ln > lim:
                dx, dy = dx * lim / ln, dy * lim / ln
            if ons[p]:
                disp[k] = (dx, dy)
            else:
                disp[k] = None
        # 控制点用相邻 on-curve 点位移的平均
        for k in range(m):
            if disp[k] is not None:
                nxs[idx[k]] = xs[idx[k]] + disp[k][0]
                nys[idx[k]] = ys[idx[k]] + disp[k][1]
        for k in range(m):
            if disp[k] is None:
                pm = None
                pn = None
                for s in range(1, m + 1):
                    if disp[(k - s) % m] is not None:
                        pm = disp[(k - s) % m]
                        break
                for s in range(1, m + 1):
                    if disp[(k + s) % m] is not None:
                        pn = disp[(k + s) % m]
                        break
                if pm and pn:
                    dx, dy = (pm[0] + pn[0]) * 0.5, (pm[1] + pn[1]) * 0.5
                else:
                    dx, dy = (pm or pn or (0.0, 0.0))
                nxs[idx[k]] = xs[idx[k]] + dx
                nys[idx[k]] = ys[idx[k]] + dy
    return nxs, nys, ons, ends
