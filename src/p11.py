# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess

def replacetabs(s):
    return s.replace("\t", " ")

if __name__ == '__main__':
    print("python version:")
    with open(sys.argv[1], 'r') as f:
        for line in f:
            print(replacetabs(line), end="")

    cmd = "sed 's/\t/ /g' ../dat/hightemp.txt"
    print("sed: ")
    subprocess.call(cmd, shell=True)

    cmd = 'cat ../dat/hightemp.txt | tr -s "\t" " "'
    print("tr: ")
    subprocess.call(cmd, shell=True)

    cmd = "expand -t 1 ../dat/hightemp.txt"
    print("expand: ")
    subprocess.call(cmd, shell=True)
