# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


if __name__ == '__main__':
    s = "パタトクカシーー"
    cut = [c for i,c in enumerate(s) if i%2 == 0]
    print("".join(cut))
