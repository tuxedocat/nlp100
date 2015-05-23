# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks, visualize_dependency
import pydot


if __name__ == '__main__':
    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    punct_p = lambda x: False if x in ["、", "。", "。。"] else True
    parsed = add_chunks(morphs)
    sent = parsed[7]
    visualize_dependency(sent, "../out/p44/test.dot")
    for i, sent in enumerate(parsed):
        visualize_dependency(sent, "../out/p44/sent{}.png".format(i))
        if i > 100:
            break
