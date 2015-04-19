# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        wcl = len(f.readlines())

    print("python version:\n{}\n".format(wcl))
    cmd = "wc -l ../dat/hightemp.txt"
    print("wc -l: ")
    subprocess.call(cmd, shell=True)
