# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks


def is_noun_in_chunk(morphs):
    return any([m.pos == "名詞" for m in morphs])


def is_verb_in_chunk(morphs):
    return any([m.pos == "動詞" for m in morphs])

if __name__ == '__main__':
    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    punct_p = lambda x: False if x in ["、", "。", "。。"] else True
    parsed = add_chunks(morphs)
    for sent in parsed:
        for srcc in sent:
            if is_noun_in_chunk(srcc.morphs):
                _s = srcc.chunktext(punct_p)
                try:
                    dstc = sent[srcc.dst]
                    if is_verb_in_chunk(dstc.morphs):
                        _d = dstc.chunktext(punct_p)
                        print("{src}\t{dst}".format(src=_s, dst=_d))
                except IndexError:
                    print("{src}\t{dst}".format(src=_s, dst=""))
