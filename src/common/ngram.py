# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


def ngram(s=None, n=2):
    """Return n-grams for given list or string"""
    try:
        s = s.split()
    except AttributeError:
        pass

    ngrams = []

    for i, w in enumerate(s):
        try:
            ngrams.append(s[i:i+n])
        except IndexError:
            pass

    ngrams = [tuple(l) for l in ngrams if len(l)==n]
    return ngrams


if __name__ == '__main__':
    print(ngram("my sad cat sat on the mat which he liked so much.", 3))
