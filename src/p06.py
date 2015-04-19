# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.ngram import ngram

if __name__ == '__main__':
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = set(ngram([c for c in s1], 2))
    Y = set(ngram([c for c in s2], 2))
    print("Union", X.union(Y))
    print("Intersection", X.intersection(Y))
    print("Difference", X.difference(Y))
    se = ('s', 'e')
    if se in X:
        print("s e is in X")
    if se in Y:
        print("s e is in Y")
