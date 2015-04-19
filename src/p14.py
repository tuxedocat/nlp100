# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess
from docopt import docopt

if __name__ == '__main__':
    __doc__ = ( """Simplified implementation of head command. \n\n"""
                """usage: \n"""
                """  p14.py [-n <N>] <file>... \n\n"""
                """options: \n"""
                """  -n <N>     lines to show. [default: 10]""")

    args = docopt(__doc__)
    n = int(args["-n"]) if "-n" in args else 10

    for f in args["<file>"]:
        with open(f, 'r') as input:
            for i, line in enumerate(input):
                if i+1 <= n:
                    print(line, end="")
                else:
                    break

    cmd = "head -n 10 ../dat/hightemp.txt"
    print("head 10: ")
    subprocess.call(cmd, shell=True)
