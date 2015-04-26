# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import sys
import MeCab
import pickle

def get_np(sentencelist: list) -> list:
    """Find pattern <noun> の_助詞_連体化 <noun>"""
    nplist = []
    for _l in sentencelist:
        noid = []
        _nplist = []

        if _l:
            for i, _d in enumerate(_l):
                if _d["surface"] == "の" and _d["pos"] == "助詞":
                    noid.append(i)
            if noid:
                for i in noid:
                    try:
                        no = _l[i]
                        _a = _l[i-1] if _l[i-1]["pos"] == "名詞" else None
                        _b = _l[i+1] if _l[i+1]["pos"] == "名詞" else None
                    except IndexError:
                        _a, _b = None, None
                    if _a and _b:
                        _nplist.append((_a, no, _b))
        if _nplist:
            nplist.append(_nplist)
    return nplist


if __name__ == '__main__':
    with open('../dat/neko.txt.dic','rb') as f:
        parsed = pickle.load(f)

    nplist = get_np(parsed)
