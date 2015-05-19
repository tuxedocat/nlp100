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


def get_dependency(chunklist):
    chains = []
    for i, chunk in enumerate(chunklist):
        if is_noun_in_chunk(chunk.morphs):
            nxt = chunk.dst
            chain = [chunk.chunktext(punct_p)]
            while nxt > 0:
                try:
                    dstchunk = chunklist[nxt]
                    dstname = dstchunk.chunktext(punct_p)
                    chain.append(dstname)
                    nxt = dstchunk.dst
                except:
                    break
            if len(chain) >= 2:
                chains.append(" -> ".join(chain))
    return chains


if __name__ == '__main__':
    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    punct_p = lambda x: False if x in ["、", "。", "。。"] else True
    parsed = add_chunks(morphs)
    for i, sent in enumerate(parsed):
        chains = get_dependency(sent)
        if chains:
            for c in chains:
                print(c)
