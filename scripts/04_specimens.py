"""04  生成高端多语言样张（build/specimen/）

全部用可变字体本身渲染（PIL + FreeType 轴控制），所见即真实字形。
版式：白底、克制黑白灰、细分割线、大留白；覆盖简繁中、英、日、韩、
欧洲变音字母、希腊/西里尔、假名与常用符号。
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
PAPER = (255, 255, 255)

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


def canvas(w, h, bg=PAPER):
    img = Image.new('RGB', (w * SS, h * SS), bg)
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

    # ---------------- 01 封面 hero
    W, H = 1240, 760
    img, dr = canvas(W, H)
    L(dr, (72, 72), 'HOWSENLIU FANGRUN  ·  TYPEFACE 2.000', 12, color=GREY, wght=600)
    rule(dr, 72, 108, W - 72)

    T(dr, (72, 208), '柳皓升方润黑体', 92, wght=500)
    T(dr, (74, 326), 'HowsenLiu Fangrun', 40, wght=300, ink=GREY)
    T(dr, (74, 392), '方折骨架，圆润收口。Square skeleton, soft terminals.', 22, ink=BODY)

    y = 512
    langs = [
        ('简体中文', '柳皓升方润黑体'),
        ('繁體中文', '柳皓升方潤黑體'),
        ('English', 'HowsenLiu Fangrun'),
        ('日本語', '柳皓升方潤ゴシック'),
        ('한국어', '柳皓升방운고딕'),
    ]
    col_w = (W - 144) / 5
    for i, (tag, word) in enumerate(langs):
        x = 72 + i * col_w
        L(dr, (x, y), tag, 11, color=FAINT)
        T(dr, (x, y + 22), word, 20, wght=400)
    T(dr, (72, H - 64), '44,731 字形 · 44,828 码位  ·  简繁中 / 谚文 / 假名 / 拉丁 / 希腊 / 西里尔  ·  SIL OFL 1.1',
      13, ink=GREY)
    save(img, W, H, 'hero.png')

    # ---------------- 02 字重轴
    W, H = 1240, 720
    img, dr = canvas(W, H)
    L(dr, (72, 56), 'WEIGHT  ·  wght 100 – 700', 12, color=GREY, wght=600)
    T(dr, (72, 84), '同一骨架，四档粗细', 34)

    y = 180
    rows = [(100, 'Light 100'), (400, 'Regular 400'), (500, 'Medium 500'), (700, 'Bold 700')]
    for wg, name in rows:
        L(dr, (72, y + 26), name, 12)
        T(dr, (288, y), 'Aa 柳皓升方润黑体 0123456789', 46, wght=wg)
        y += 112
        rule(dr, 72, y - 28, W - 72)
    T(dr, (72, H - 56), '字重变化只加厚笔画；圆角半径、中宫与结构比例保持不变。', 14, ink=GREY)
    save(img, W, H, 'spec-weights.png')

    # ---------------- 03 多语言样张
    W, H = 1240, 920
    img, dr = canvas(W, H)
    L(dr, (72, 56), 'MULTILINGUAL  ·  同一副骨架，横跨多种文字', 12, color=GREY, wght=600)

    blocks = [
        ('简体中文 · Simplified Chinese', '柳皓升方润黑体', '方圆之间，温润而坚定'),
        ('繁體中文 · Traditional Chinese', '柳皓升方潤黑體', '方圓之間，溫潤而堅定'),
        ('English', 'HowsenLiu Fangrun', 'Between square and softness'),
        ('日本語 · Japanese', '柳皓升方潤ゴシック', '角と丸みのあいだ'),
        ('한국어 · Korean', '柳皓升방운고딕', '네모난 골격, 부드러운 모서리'),
        ('European · 欧洲语言', 'ÀÉÎÕÜ ñéüöß', 'Café · Grün · São · € £ ¥'),
    ]
    col_w = (W - 144 - 48) / 2
    row_h = 224
    for i, (tag, big, sub) in enumerate(blocks):
        col, row = i % 2, i // 2
        x = 72 + col * (col_w + 48)
        y = 132 + row * row_h
        rule(dr, x, y, x + col_w)
        L(dr, (x, y + 24), tag, 12, color=FAINT)
        T(dr, (x, y + 58), big, 38, wght=500)
        T(dr, (x, y + 128), sub, 18, ink=GREY)

    y = 132 + 3 * row_h
    rule(dr, 72, y, W - 72)
    L(dr, (72, y + 24), 'SYMBOLS · 标点与常用符号', 12, color=FAINT)
    T(dr, (72, y + 58), '，。、！？：；（）「」《》—…·★☆◆◇○●→←↑↓ € £ ¥ © ® ™', 26, ink=BODY)
    save(img, W, H, 'spec-multilingual.png')

    # ---------------- 04 正文排版
    W, H = 1240, 820
    img, dr = canvas(W, H)
    L(dr, (72, 56), 'TEXT  ·  正文排版', 12, color=GREY, wght=600)
    T(dr, (72, 88), '方中带圆，温润如玉', 40, wght=500)

    zh = ('柳皓升方润黑体以略方的骨架为底，在每一处笔画交接与端点都做了同一半径的圆角处理。'
          '它不靠装饰取胜，而是让方块结构在细节处变得温和，长句阅读时保持稳定与安静。')
    en = ('Because every master shares one skeleton, the interpolation never distorts: '
          'contour counts, point counts and point order are identical across all eight masters.')
    T(dr, (72, 176), zh, 17, ink=BODY, spacing=12, wrap=30)
    T(dr, (660, 176), en, 16, ink=BODY, spacing=12, wrap=28)

    rule(dr, 72, 470, W - 72)
    L(dr, (72, 500), '日本語 · 本文組版', 12, color=FAINT)
    T(dr, (72, 528), '少し角張った骨格をベースに、角と末端を同じ半径で丸めたゴシック体。', 18, ink=BODY)
    L(dr, (72, 592), '한국어 · 본문 조판', 12, color=FAINT)
    T(dr, (72, 620), '약간 각진 골격을 바탕으로 획의 이음새와 끝을 같은 반지름으로 둥글게 처리했습니다.', 18, ink=BODY)

    T(dr, (72, H - 96), '17 pt · wght 400 · wdth 100 · opsz 16', 13, ink=GREY)
    T(dr, (72, H - 64), '行距 1.85 · 字距 0.01 em', 13, ink=GREY)
    save(img, W, H, 'spec-text.png')

    # ---------------- 05 字符集
    W, H = 1240, 880
    img, dr = canvas(W, H)
    L(dr, (72, 56), 'CHARSET  ·  字符覆盖', 12, color=GREY, wght=600)

    rows = [
        ('汉字 Han', '柳皓升方润黑体 结构骨架 温润 端正 谦和 安宁 稳重'),
        ('日文假名 Kana', 'あいうえお かきくけこ さしすせそ アイウエオ カキクケコ'),
        ('谚文 Hangul', '가나다라마바사 아자차카타파하 글로벌 한국어 폰트'),
        ('拉丁 / 欧洲 Latin', 'ABCDEFGH a b c d e f g h Ñ É Ü ß Ø Ç ñ é ü ö € ¥'),
        ('希腊 / 西里尔 Greek · Cyrillic', 'ΑΒΓΔ αβγδ Ддбвж Ллмф Йй'),
        ('标点符号 Symbols', '，。！？· ★ ☆ ◆ ◇ ○ ● → ← ↑ ↓ № § © ® ™'),
    ]
    y = 132
    for tag, sample in rows:
        L(dr, (72, y), tag, 12, color=FAINT)
        T(dr, (300, y - 6), sample, 22, ink=BODY)
        y += 96
        rule(dr, 72, y - 24, W - 72)

    T(dr, (72, H - 96), '44,731 字形 · 44,828 码位', 16, wght=600)
    T(dr, (72, H - 62), '覆盖 GBK 全集、GB 18030 一/二级汉字、Big5 繁体；11,172 个谚文预组音节与 Jamo；'
                         '平假名 / 片假名；注音符号；拉丁扩展、希腊、西里尔；上标 / 下标 / 修饰字母与常用标点符号。',
      13, ink=GREY)
    save(img, W, H, 'spec-charset.png')


if __name__ == '__main__':
    main()
