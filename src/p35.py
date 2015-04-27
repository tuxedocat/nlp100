# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import sys
import MeCab
import pickle


def filter_nn(sublist: list) -> list:
    filtered = []
    _ = []
    for d in sublist:
        if d:
            _.append(d)
        else:
            filtered.append(_)
            _ = []
    print(filtered)
    return [l for l in filtered if len(l) >= 2]


def get_nn(sentencelist: list) -> list:
    """Find maximum sequence of noun noun ..."""
    nnlist = []
    for _l in sentencelist:
        _nnlist = []
        _nplist = []

        if _l:
            for i, _d in enumerate(_l):
                if _d["pos"] == "名詞":
                    _nnlist.append(_d)
                else:
                    _nnlist.append(None)

            nnlist.append(filter_nn(_nnlist))
    return nnlist


if __name__ == '__main__':
    with open('../dat/neko.txt.dic', 'rb') as f:
        parsed = pickle.load(f)

    nnlist = get_nn(parsed)
