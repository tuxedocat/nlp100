# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import sys
import pickle
from collections import Counter
from itertools import chain


class WordFreq:

    def __init__(self, parsed):
        self.parsed = parsed
        self.counter = None

    def count(self):
        suflist = [d["surface"]
                   for d in list(chain.from_iterable(self.parsed))]
        self.counter = Counter(suflist)
        return self.counter

if __name__ == '__main__':
    with open('../dat/neko.txt.dic', 'rb') as f:
        parsed = pickle.load(f)

    wf = WordFreq(parsed)
    wordfreq = wf.count()
    sortedbyfreq = sorted(wordfreq.items(), key=lambda x: x[1], reverse=True)
