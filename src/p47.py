# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks


def get_leftmostxx_func(pos):
    def get_xx(morphs):
        for morph in morphs:
            if morph.pos == pos:
                return morph.base
        return ""

    return get_xx


def is_sahen_vp(morphs):
    for i, m in enumerate(morphs):
        if m.pos1 == "サ変接続":
            try:
                n = morphs[i + 1]
                if n.pos1 == "格助詞" and n.surface == "を":
                    return True
            except:
                return False
    return False

if __name__ == '__main__':
    get_leftmostverb = get_leftmostxx_func("動詞")
    get_particle = get_leftmostxx_func("助詞")
    punct_p = lambda x: False if x in ["、", "。", "。。"] else True

    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    parsed = add_chunks(morphs)
    predcases = []
    for sent in parsed:
        for srcc in sent:
            particles = []
            words = []
            if is_sahen_vp(srcc.morphs):
                npid = srcc.srcs[0]
                npdepto = srcc.dst
                vp = sent[npdepto]
                if vp:
                    particles = [get_particle(ph.morphs) for i, ph in enumerate(sent) if ph.dst == vp.srcs[0]]
                    words = [ph.chunktext(filter_p=punct_p) for i, ph in enumerate(sent) if ph.dst == vp.srcs[0]]
                    if particles and words:
                        predcases.append((srcc.chunktext_vbase(filter_p=punct_p)+get_leftmostverb(vp.morphs),                         zip(particles, words)))

    for t in predcases:
        vp = t[0]
        _p = list(t[1])
        parts = [p[0] for p in _p]
        np = [p[1] for p in _p]
        print("{v}\t{c}\t{w}".format(
            v=vp, c=" ".join(parts), w=" ".join(np)))
