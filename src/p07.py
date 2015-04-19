# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


def boilerplate(x="", y="", z=""):
    return "{0}時の{1}は{2}".format(x, y, z)

if __name__ == '__main__':
    print(boilerplate(12, "気温", 22.4))
