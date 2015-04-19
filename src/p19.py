# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess
from docopt import docopt
from collections import Counter

filepath = "../dat/hightemp.txt"

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input:
        col1 = [l.split("\t")[0] for l in input]
    counts = Counter(col1)
    total = sum(counts.values())
    for pair in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print("{word}\t{c}".format(word=pair[0], c=pair[1]))

    print("\nsort command:")
    cmd = 'cat {} | cut -f1 | sort -r -k 1 | uniq -c | sort -r -n -k 1'.format(filepath)
    subprocess.call(cmd, shell=True)
