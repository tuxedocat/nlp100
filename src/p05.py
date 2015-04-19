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

    ngrams = [l for l in ngrams if len(l)==n]
    return(ngrams)


if __name__ == '__main__':
    s = "I am an NLPer"
    c = [c for c in s]
    wordbigram = ngram(s, 2)
    charbigram = ngram(c, 2)
    print("Word Bi-gram")
    print(wordbigram)
    print("Character Bi-gram")
    print(charbigram)
