# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess


if __name__ == '__main__':
    print("python version:")
    with open(sys.argv[1], 'r') as f:
        c1 = [l.strip("\n") for l in f.readlines()]
    with open(sys.argv[2], 'r') as f:
        c2 = [l.strip("\n") for l in f.readlines()]
    with open("./colmerged.txt", "w") as f:
        for line in zip(c1, c2):
            f.write("\t".join(line)+"\n")

    cmd = "cat ./colmerged.txt"
    subprocess.call(cmd, shell=True)

    cmd = "paste -d '\t' col1.txt col2.txt"
    print("paste: ")
    subprocess.call(cmd, shell=True)
