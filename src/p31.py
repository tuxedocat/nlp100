# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import sys
import MeCab
import pickle

if __name__ == '__main__':
    with open('../dat/neko.txt.dic','rb') as f:
        parsed = pickle.load(f)

    v_surfaces = [[d.get("surface") for d in s if s is not None and d['pos'] == "動詞"]
                   for s in parsed]
