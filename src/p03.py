# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import re

if __name__ == '__main__':
    sentence = ("""Now I need a drink, """
                """alcoholic of course, """
                """after the heavy lectures involving quantum mechanics.""")
    alpha = re.compile("\w")
    counts = [len(alpha.findall(sub)) for sub in sentence.split()]
    print(counts)
