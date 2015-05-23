# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks, get_leftmostxx_func, punct_p


if __name__ == '__main__':
    get_leftmostverb = get_leftmostxx_func("動詞")
    get_particle = get_leftmostxx_func("助詞")

    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    parsed = add_chunks(morphs)
    predcases = []
    for sent in parsed:
        for srcc in sent:
            pred = get_leftmostverb(srcc.morphs)
            particles = []
            words = []
            if pred:
                predid = srcc.srcs[0] if srcc.srcs else -1
                if predid >= 0:
                    for c in sent:
                        if c.dst == predid:
                            _p = get_particle(c.morphs)
                            if _p:
                                particles.append(_p)
                                words.append(c.chunktext(filter_p=punct_p))
            if pred and particles:
                predcases.append((pred, zip(particles, words)))
            pred = ""
            particles = []
            words = []

    for t in predcases:
        verb = t[0]
        case = sorted(t[1], key=lambda x: x[0])
        particles = [p[0] for p in case]
        words = [p[1] for p in case]
        print("{v}\t{c}\t{w}".format(
            v=verb, c=" ".join(particles), w=" ".join(words)))
