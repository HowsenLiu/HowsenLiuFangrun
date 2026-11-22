"""10  生成页面演示用的极小 woff2 子集（只含 index.html 实际用到的字符）"""
import os
import re

from fontTools.ttLib import TTFont
from fontTools import subset as ftsub

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VF = os.path.join(ROOT, 'build', 'HowsenLiuFangrun-VF.ttf')
OUT_DIR = os.path.join(ROOT, 'build', 'webfonts')
HTML = os.path.join(os.path.dirname(ROOT), '发布包', '2_网页部署_CloudflarePages',
                    'site', 'index.html')

EXTRA = ('永和圆方润皓升字体设计可变光学尺寸宽度重量柳'
         '가나다라마바사아자차카타파하글로벌한국어폰트설계방운고딕'
         '0123456789'
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         'abcdefghijklmnopqrstuvwxyz'
         '—…·～！。，、；：？“”‘’（）《》〈〉←→↑↓')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    raw = open(HTML, encoding='utf-8').read()
    body = re.sub(r'<[^>]+>', ' ', raw)          # 去掉标签，只留正文
    body = re.sub(r'(?s)<script.*?</script>', ' ', body)
    js = open(os.path.join(os.path.dirname(HTML), 'js', 'main.js'), encoding='utf-8').read()
    chars = set(body) | set(js) | set(EXTRA)
    chars |= set(' \u00a0')

    opts = ftsub.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = ['*']
    opts.desubroutinize = True
    opts.drop_tables = []

    f = TTFont(VF)
    s = ftsub.Subsetter(options=opts)
    s.populate(text=''.join(sorted(chars)))
    s.subset(f)
    p = os.path.join(OUT_DIR, 'HowsenLiuFangrun-VF-demo.woff2')
    f.save(p)
    print(f'  demo 子集: {os.path.getsize(p) / 1e6:.2f} MB '
          f'({f["maxp"].numGlyphs} 字形 / {len(chars)} 字符)')


if __name__ == '__main__':
    main()
