# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import sys
import MeCab
import pickle


def morph2dict(line):
    """parse a line of mecab's output, and put them into a dict"""
    d = {}
    _ = line.strip().split('\t')
    try:
        _meta = _[1].split(',')
        d["surface"] = _[0]
        d["pos"] = _meta[0]
        d["pos1"] = _meta[1]
        d["base"] = _meta[6]
        return d
    except IndexError:
        return None

if __name__ == '__main__':
    """Read tagged data of mecab and export a list of dicts"""
    with open('../dat/neko.txt.mecab', 'r') as f:
        tagged = f.read().split("EOS")

    packed = [
        [morph2dict(l) for l in s.split("\n") if morph2dict(l)] for s in tagged]
    with open('../dat/neko.txt.dic', 'wb') as f:
        pickle.dump(packed, f)
