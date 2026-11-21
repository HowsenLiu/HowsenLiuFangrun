"""04  生成三轴样张（build/specimen/）

全部用可变字体本身渲染（PIL + FreeType 轴控制），所见即真实字形。
"""
from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VF = os.path.join(ROOT, 'build', 'HowsenLiuFangrun-VF.ttf')
OUT = os.path.join(ROOT, 'build', 'specimen')
SS = 2                       # 超采样倍数
INK = (23, 23, 26)
BODY = (43, 43, 48)
GREY = (113, 113, 122)
FAINT = (161, 161, 170)
LINE = (231, 231, 234)

_cache = {}


def font(size, wght=400, wdth=100, opsz=16):
    key = (size, wght, wdth, opsz)
    if key in _cache:
        return _cache[key]
    f = ImageFont.truetype(VF, int(size * SS))
    try:
        f.set_variation_by_axes([wght, wdth, opsz])
    except Exception as exc:
        print('   轴设置失败', key, exc)
    _cache[key] = f
    return f


def canvas(w, h):
    img = Image.new('RGB', (w * SS, h * SS), 'white')
    return img, ImageDraw.Draw(img)


def save(img, w, h, name):
    img = img.resize((w, h), Image.LANCZOS)
    img.save(os.path.join(OUT, name), optimize=True)
    print('  ', name)


def wrap_cjk(text, n):
    """按字符数硬换行（PIL 不自动折行；含空格的英文按词折行）。"""
    if ' ' in text:
        words, out, line = text.split(' '), [], ''
        for w in words:
            if line and len(line) + 1 + len(w) > n:
                out.append(line)
                line = w
            else:
                line = f'{line} {w}'.strip()
        if line:
            out.append(line)
        return '\n'.join(out)
    out, line = [], ''
    for ch in text:
        line += ch
        if len(line) >= n:
            out.append(line)
            line = ''
    if line:
        out.append(line)
    return '\n'.join(out)


def T(dr, xy, text, size, wght=400, wdth=100, opsz=16, ink=INK, spacing=0, wrap=0):
    if wrap:
        text = wrap_cjk(text, wrap)
    dr.multiline_text((xy[0] * SS, xy[1] * SS), text,
                      font=font(size, wght, wdth, opsz), fill=ink,
                      spacing=spacing * SS)


def L(dr, xy, text, size=13, color=GREY, wght=500):
    T(dr, xy, text, size, wght=wght, ink=color)


def rule(dr, x1, y, x2, color=LINE, width=1):
    dr.line((x1 * SS, y * SS, x2 * SS, y * SS), fill=color, width=max(1, width * SS))


def main():
    os.makedirs(OUT, exist_ok=True)

    # ---------------- 01 总览
    W, H = 1240, 900
    img, dr = canvas(W, H)
    T(dr, (64, 40), '柳皓升方润黑体', 84, wght=500)
    T(dr, (66, 140), 'HowsenLiu Fangrun Variable  ·  wght × wdth × opsz', 26, wght=300, ink=GREY)
    T(dr, (66, 184), '一个骨架，三种呼吸。', 30)
    y = 258
    rows = [('wght', '100 → 700', '100  Light', 100, 100),
            ('wght', '100 → 700', '400  Regular', 400, 100),
            ('wght', '100 → 700', '700  Bold', 700, 100),
            ('wdth', '75 → 105', '75  Condensed', 400, 75),
            ('wdth', '75 → 105', '105  Expanded', 400, 105)]
    for tag, rng, sample, wg, wd in rows:
        L(dr, (66, y + 16), f'{tag}  {rng}', 12)
        T(dr, (66, y + 36), sample, 14, ink=GREY)
        T(dr, (206, y + 2), '永 和 圆 方 润 皓 升 字', 44, wght=wg, wdth=wd)
        y += 88
        rule(dr, 66, y - 16, W - 66)

    L(dr, (66, y + 6), 'opsz  12 → 72', 12)
    T(dr, (66, y + 26), '12  Caption', 14, ink=GREY)
    T(dr, (206, y), '小字加粗、中宫放大', 40, opsz=12)
    T(dr, (836, y), '大字收细、细节精致', 40, opsz=72)
    L(dr, (206, y + 52), '42 pt  ·  opsz 12', 12, color=FAINT)
    L(dr, (836, y + 52), '42 pt  ·  opsz 72', 12, color=FAINT)
    T(dr, (66, H - 56), '44,000+ 字符  ·  中文 / 日文 / 谚文  ·  SIL OFL 1.1  ·  免费商用', 14, ink=GREY)
    save(img, W, H, '01-overview.png')

    # ---------------- 02 字重
    W, H = 1240, 780
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'WEIGHT  wght 100 – 700', 12)
    T(dr, (64, 66), 'HowsenLiu Fangrun', 34)
    y = 138
    for wg, name in ((100, 'Light 100'), (400, 'Regular 400'),
                     (500, 'Medium 500'), (700, 'Bold 700')):
        L(dr, (64, y + 34), name, 12)
        T(dr, (230, y), '柳皓升方润黑体 Aa 0123', 52, wght=wg)
        y += 104
        rule(dr, 64, y - 22, W - 64)
    save(img, W, H, '02-weights.png')

    # ---------------- 03 字宽
    W, H = 1240, 700
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'WIDTH  wdth 75 – 105', 12)
    T(dr, (64, 66), '字宽轴：同一骨架，横向量变', 34)
    y = 142
    for wd, name in ((75, 'Condensed 75'), (100, 'Normal 100'), (105, 'Expanded 105')):
        L(dr, (64, y + 30), name, 12)
        T(dr, (232, y), '方润黑体 可变字宽 HowsenLiu', 42, wdth=wd)
        y += 96
        rule(dr, 64, y - 20, W - 64)
    T(dr, (64, H - 110), '窄体用于标题与信息密集的版面，宽体适合品牌与海报。', 15, ink=GREY)
    save(img, W, H, '03-width.png')

    # ---------------- 04 光学尺寸
    W, H = 1240, 780
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'OPTICAL SIZE  opsz 12 – 72', 12)
    T(dr, (64, 66), '同一字号，不同光学尺寸', 34)

    L(dr, (64, 138), '正文 13 px · opsz 12 与 16 对照', 12)
    para = ('中文字体的可读性，来自笔画与中宫的比例。小字需要更实的笔画、'
            '更开的中宫，才能在小尺寸下站得住；大字则应收细笔画、'
            '收紧细节，让结构与留白更精致。')
    T(dr, (64, 172), para, 13, opsz=12, ink=BODY, spacing=9, wrap=28)
    T(dr, (664, 172), para, 13, opsz=16, ink=BODY, spacing=9, wrap=28)
    L(dr, (64, 352), 'opsz 12 · Caption', 12)
    L(dr, (664, 352), 'opsz 16 · Text（默认）', 12)
    rule(dr, 64, 380, W - 64)

    L(dr, (64, 410), '标题 88 px · 同字号、两端光学尺寸', 12)
    T(dr, (64, 442), '方润黑体', 88, wght=700, opsz=72)
    T(dr, (664, 442), '方润黑体', 88, wght=700, opsz=12)
    L(dr, (64, 606), 'opsz 72 · 笔画收细、细节精致', 12)
    L(dr, (664, 606), 'opsz 12 · 笔画加粗、中宫放大', 12)
    T(dr, (64, H - 56), 'opsz 默认 16；12–16 适配正文，24–72 适配标题与展示。', 14, ink=GREY)
    save(img, W, H, '04-optical.png')

    # ---------------- 05 文本
    W, H = 1240, 880
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'TEXT  正文排版', 12)
    T(dr, (64, 66), '方中带圆，温润如玉', 44, wght=500)
    body = [
        '柳皓升方润黑体以略方的骨架为底，在每一处笔画交接与端点都做了同一半径的圆角处理。'
        '它不靠装饰取胜，而是让方块结构在细节处变得温和，长句阅读时保持稳定与安静。',
        '同一套骨架派生出字重、字宽与光学尺寸三根轴：字重从 100 到 700 连续可调，'
        '字宽从 75 的窄体到 105 的宽体，光学尺寸则让 12 号正文与 72 号标题各有各的笔画分寸。',
        'Because every master shares one skeleton, the interpolation never distorts: '
        'contour counts, point counts and point order are identical across all eight masters.',
    ]
    y = 168
    for i, p in enumerate(body):
        T(dr, (64, y), p, 17, ink=BODY, spacing=11, wrap=62)
        y += 132
    T(dr, (64, H - 110), '17 pt · wght 400 · wdth 100 · opsz 16', 13, ink=GREY)
    T(dr, (64, H - 82), '行距 1.85 · 字距 0.01 em', 13, ink=GREY)
    save(img, W, H, '05-text.png')

    # ---------------- 06 字符集
    W, H = 1240, 880
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'CHARSET  字符集', 12)
    txt_path = ('C:\\Users\\12784\\Desktop\\字体\\柳皓升方润黑体-发布包\\发布包'
                '\\1_GitHub仓库上传\\sources\\charset\\webfont-subset.txt')
    chars = [c for c in open(txt_path, encoding='utf-8').read()
             if '\u4e00' <= c <= '\u9fff'][:600]
    x, y, per = 64, 88, 28
    for i, ch in enumerate(chars):
        if i and i % per == 0:
            x, y = 64, y + 28
        T(dr, (x, y), ch, 19)
        x += 38
    T(dr, (64, H - 50), '共 44,000+ 字形 · 覆盖 GBK 全集、GB 18030 一/二级汉字与全套谚文音节', 13, ink=GREY)
    save(img, W, H, '06-charset.png')

    # ---------------- 07 圆角细节
    W, H = 1240, 640
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'CORNER  88 / 1000 em · 统一圆角', 12)
    for i, (wg, name) in enumerate(((100, 'Light 100'), (400, 'Regular 400'),
                                    (700, 'Bold 700'))):
        L(dr, (64 + i * 400, 92), name, 13)
        T(dr, (64 + i * 400, 116), '永', 200, wght=wg)
        T(dr, (64 + i * 400 + 225, 280), '口', 92, wght=wg)
        T(dr, (64 + i * 400 + 330, 280), '口', 92, wght=wg, opsz=72)
    T(dr, (64, H - 50),
      '所有角与端点使用同一半径；字重变化只加厚笔画，不改圆角规则。右侧对比 opsz 72。',
      13, ink=GREY)
    save(img, W, H, '07-corners.png')

    # ---------------- 08 拉丁与符号
    W, H = 1240, 600
    img, dr = canvas(W, H)
    L(dr, (64, 44), 'LATIN & SYMBOLS', 12)
    T(dr, (64, 74), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 38, wght=300)
    T(dr, (64, 128), 'abcdefghijklmnopqrstuvwxyz 0123456789', 38)
    T(dr, (64, 190), 'ÀÉÎÕÜ  áéíóú  çñß  € £ $ ¥ © ® ™', 30)
    T(dr, (64, 240), '！。，、；：？“”‘’（）《》〈〉—…·～', 30)
    T(dr, (64, 290), '← → ↑ ↓ ✓ ✗ ★ ☆ ▲ △ ● ○ ■ □ ◆ ◇', 30)
    T(dr, (64, 348), 'The quick brown fox jumps over the lazy dog.  0123456789', 26, ink=BODY)
    T(dr, (64, 400), '가 나 다 라 마 바 사 아 자 차 카 타 파 하  ·  한국어 글꼴', 30)
    T(dr, (64, H - 56), '中西韩文共用同一笔画与圆角规则，混排时保持同一种语气。', 14, ink=GREY)
    save(img, W, H, '08-latin.png')


if __name__ == '__main__':
    main()
