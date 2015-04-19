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
    c1 = []
    c2 = []
    with open(sys.argv[1], 'r') as f:
        for l in f:
            c1.append(l.split("\t")[0])
            c2.append(l.split("\t")[1])

    with open("./col1.txt", "w") as f:
        for line in c1:
            f.write(line+"\n")

    with open("./col2.txt", "w") as f:
        for line in c2:
            f.write(line+"\n")

    cmd = "cut -d '\t' -f 1 ../dat/hightemp.txt"
    print("col1 cut: ")
    subprocess.call(cmd, shell=True)

    cmd = "cut -d '\t' -f 2 ../dat/hightemp.txt"
    print("col2 cut: ")
    subprocess.call(cmd, shell=True)
