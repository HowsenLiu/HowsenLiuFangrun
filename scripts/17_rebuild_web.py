"""17  VF 元数据修好后重建三个 woff2（全量 / GB2312 子集 / 页面演示子集）"""
import os
import re

from fontTools.ttLib import TTFont
from fontTools import subset as ftsub

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VF = os.path.join(ROOT, 'build', 'HowsenLiuFangrun-VF.ttf')
OUT = os.path.join(ROOT, 'build', 'webfonts')
GH_CHARSET = (r'C:\Users\12784\Desktop\字体\柳皓升方润黑体-发布包\发布包'
              r'\1_GitHub仓库上传\sources\charset\webfont-subset.txt')
HTML = os.path.join(os.path.dirname(ROOT), '发布包', '2_网页部署_CloudflarePages',
                    'site', 'index.html')

EXTRA = ('永和圆方润皓升字体设计可变光学尺寸宽度重量柳'
         '国日田力加互京华符标点数网页版权授免费商用开源软师制排印屏显'
         '가나다라마바사아자차카타파하글로벌한국어폰트설계방운고딕'
         '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
         '—…·～！。，、；：？“”‘’（）《》〈〉←→↑↓')


def save_woff2(font, path):
    font.flavor = 'woff2'
    font.save(path)
    print(f'  {os.path.basename(path)}: {os.path.getsize(path) / 1e6:.2f} MB '
          f'({font["maxp"].numGlyphs} 字形)')


def subset(text, path):
    opts = ftsub.Options()
    opts.layout_features = ['*']
    opts.name_IDs = ['*']
    opts.desubroutinize = True
    opts.drop_tables = []
    f = TTFont(VF)
    s = ftsub.Subsetter(options=opts)
    s.populate(text=text)
    s.subset(f)
    save_woff2(f, path)


def main():
    os.makedirs(OUT, exist_ok=True)
    save_woff2(TTFont(VF), os.path.join(OUT, 'HowsenLiuFangrun-VF.woff2'))

    text = open(GH_CHARSET, encoding='utf-8').read()
    subset(text, os.path.join(OUT, 'HowsenLiuFangrun-VF-subset.woff2'))

    raw = open(HTML, encoding='utf-8').read()
    body = re.sub(r'(?s)<script.*?</script>', ' ', raw)
    body = re.sub(r'<[^>]+>', ' ', body)
    chars = set(body) | set(EXTRA) | {' ', '\u00a0'}
    subset(''.join(sorted(chars)), os.path.join(OUT, 'HowsenLiuFangrun-VF-demo.woff2'))


if __name__ == '__main__':
    main()
