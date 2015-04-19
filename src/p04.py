# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


if __name__ == '__main__':
    s = ("""Hi He Lied Because Boron Could Not Oxidize Fluorine. """
        """New Nations Might Also Sign Peace Security Clause. """
        """Arthur King Can.""")
    cutone = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    elements = {}
    for i, w in enumerate(s.split()):
        if i + 1 in cutone:
            elements[w[0]] = i + 1
        else:
            elements[w[:2]] = i + 1
    print(elements)
