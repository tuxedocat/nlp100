# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


from common.cabochatools import PrinterMixin, Morph, read_cabocha


if __name__ == '__main__':
    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        parsed, _ = read_cabocha(f)
    for m in parsed[2]:
        try:
            m.printmorph()
        except AttributeError:
            print(m)
