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
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class WordFreq:

    def __init__(self, parsed):
        self.parsed = parsed
        self.counter = None

    def count(self):
        suflist = [d["surface"]
                   for d in list(chain.from_iterable(self.parsed))]
        self.counter = Counter(suflist)
        self.df = pd.DataFrame.from_dict(
            self.counter.most_common(len(self.counter)))
        self.df.columns = ['word', 'count']

    def display_cui(self, n=10):
        print(self.counter.most_common(n))

    def display_bar(self, n=10):
        sns.set(style='dark', context='talk')
        x = [t[0] for t in self.counter.most_common(n)]
        y = [t[1] for t in self.counter.most_common(n)]
        plt.bar(range(n), y, align="center")
        plt.xticks(range(n), x)
        plt.show()

    def display_hist(self, bins=50):
        sns.set(style='dark', context='talk')
        y = [t[1] for t in self.counter.items()]
        plt.hist(y, bins=bins, log=True)
        plt.show()

if __name__ == '__main__':
    with open('../dat/neko.txt.dic', 'rb') as f:
        parsed = pickle.load(f)

    wf = WordFreq(parsed)
    wordfreq = wf.count()
    wf.display_cui()
    wf.display_hist()
