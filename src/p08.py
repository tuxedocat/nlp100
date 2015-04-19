# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


def cipher(input=""):
    crypted = []
    for c in input:
        if c.isalpha() and c.islower():
            crypted.append(chr(219 - ord(c)))
        else:
            crypted.append(c)
    return "".join(crypted)

if __name__ == '__main__':
    input = "My sad cat came 2 my home."
    print('input:\t {}'.format(input))
    print('\ncrypt:\t {}'.format(cipher(input)))
    print('\ndecrypt: {}'.format(cipher(cipher(input))))
