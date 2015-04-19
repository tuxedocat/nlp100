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
    col = []
    with open(sys.argv[1], 'r') as input:
        for line in input:
            col.append(line.split("\t")[0])
    print(sorted(set(col)))
