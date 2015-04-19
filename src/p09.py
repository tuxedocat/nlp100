# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

import random

def typoglycemia(s):
    """
    create typoglycemia for given sequence

    args
    ----
    s: string, assuming words are space-separated

    returns
    -------
    shuffled string, space-separated
    """
    _t = []
    for w in s.split():
        if len(w) > 4:
            _t.append(_shuffle(w))
        else:
            _t.append(w)
    return " ".join(_t)

def _shuffle(w):
    """
    shuffle characters in a word except head and tail
    """
    _w = [c for c in w]
    head = _w.pop(0)
    tail = _w.pop(-1)
    random.shuffle(_w)
    mid = "".join(_w)
    return head + mid + tail


if __name__ == '__main__':
    s = ("I couldn't believe that I could actually understand what "
         "I was reading : the phenomenal power of the human mind .")
    print(typoglycemia(s))
