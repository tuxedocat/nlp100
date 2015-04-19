# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess
import math
from docopt import docopt

if __name__ == '__main__':
    __doc__ = ( """Simplified implementation of split command. \n\n"""
                """usage: \n"""
                """  p16.py [-n <N>] <file> \n\n"""
                """options: \n"""
                """  -n <N>     num of split [default: 5]""")

    args = docopt(__doc__)
    n = int(args["-n"]) if "-n" in args else 5

    with open(args["<file>"], 'r') as input:
        text = input.readlines()
        L = len(text)
        N = math.floor(L / n)
        c = 1
        splits = []
        _s = []
        for line in text:
            if c >= N:
                _s.append(line)
                splits.append(_s)
                _s = []
                c = 1
            else:
                _s.append(line)
                c += 1

    for i, split in enumerate(splits):
        with open("./p16-split-{}.txt".format(i+1), "w") as output:
            output.writelines(split)
