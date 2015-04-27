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
    with open('../dat/neko.txt.dic', 'rb') as f:
        parsed = pickle.load(f)

    n_sahen = [[d for d in s if s is not None and d['pos'] == "名詞" and "サ変" in d['pos1']]
               for s in parsed]
