"""14  修正 fvar 轴名与命名实例名（STAT 已正确，此处只补 fvar 与 name 记录）"""
import os

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VF = os.path.join(ROOT, 'build', 'HowsenLiuFangrun-VF.ttf')

INSTANCE_NAMES = [
    ('Light', '细体'),
    ('Regular', '常规'),
    ('Medium', '中粗'),
    ('Bold', '粗体'),
    ('Condensed', '窄体'),
    ('Expanded', '宽体'),
    ('Caption', '小字'),
    ('Display Bold', '大标题粗'),
]
AXIS_IDS = {'wght': 256, 'wdth': 261, 'opsz': 265}


def add(nm, nid, en, zh=None):
    for pid, eid, lid, s in ((3, 1, 0x409, en), (3, 1, 0x804, zh)):
        if s is None:
            continue
        rec = NameRecord()
        rec.nameID, rec.platformID, rec.platEncID, rec.langID = nid, pid, eid, lid
        rec.string = s.encode('utf-16-be')
        nm.names = [r for r in nm.names if not (r.nameID == nid and r.platformID == pid
                                                and r.langID == lid)]
        nm.names.append(rec)


def main():
    f = TTFont(VF)
    nm = f['name']
    fv = f['fvar']

    for a in fv.axes:
        a.axisNameID = AXIS_IDS[a.axisTag]

    ids = []
    base = 269
    for i, (en, zh) in enumerate(INSTANCE_NAMES):
        nid = base + i * 2
        add(nm, nid, en, zh)
        ids.append(nid)
    for inst, nid in zip(fv.instances, ids):
        inst.subfamilyNameID = nid

    f.save(VF)
    g = TTFont(VF, lazy=True)
    print('axes:', [(a.axisTag, a.axisNameID, g['name'].getDebugName(a.axisNameID))
                    for a in g['fvar'].axes])
    print('instances:', [(i.coordinates['wght'], i.coordinates['wdth'], i.coordinates['opsz'],
                          g['name'].getDebugName(i.subfamilyNameID))
                         for i in g['fvar'].instances])


if __name__ == '__main__':
    main()
