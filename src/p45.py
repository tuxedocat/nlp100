# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks, get_leftmostxx_func


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
            if pred:
                predid = srcc.srcs[0] if srcc.srcs else -1
                if predid >= 0:
                    for c in sent:
                        if c.dst == predid:
                            _p = get_particle(c.morphs)
                            if _p:
                                particles.append(_p)
            if pred and particles:
                predcases.append((pred, particles))
            pred = ""
            particles = []

    for t in predcases:
        print("{v}\t{c}".format(v=t[0], c=" ".join(sorted(t[1]))))

    print(
        "# Additional commandline example (frequency of pred-particles patterns)")
    print("# python p45.py | sort | uniq -c | sort -nr")

    print("# Additional commandline example (する・見る・与える)")
    print('# python p45.py | egrep "(する|見る|与える)" | sort | uniq -c | sort -nr')
