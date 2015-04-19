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

filepath = "../dat/hightemp.txt"

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as input:
        col3sorted = sorted([l.split() for l in input.readlines()],
                          key=lambda x: float(x[2]), reverse=True)

    for line in col3sorted:
        print("\t".join(line))

    print("\nsort command:")
    cmd = 'sort -n -r -k 3 {}'.format(filepath)
    subprocess.call(cmd, shell=True)
