# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"

from common.cabochatools import read_cabocha, add_chunks
import pydot


def is_noun_in_chunk(morphs):
    return any([m.pos == "名詞" for m in morphs])


def is_verb_in_chunk(morphs):
    return any([m.pos == "動詞" for m in morphs])


def visualize_dependency(chunklist, path):
    g = pydot.Dot(graph_type='digraph')
    for i, chunk in enumerate(chunklist):
        name = chunk.chunktext(punct_p)
        try:
            dstchunk = chunklist[chunk.dst]
            dstname = dstchunk.chunktext(punct_p)
            edge = pydot.Edge(src=name, dst=dstname)
            g.add_edge(edge)
        except:
            pass
    if path.endswith(".png"):
        g.write_png(path)
    else:
        g.write_dot(path)


if __name__ == '__main__':
    with open('../dat/neko.txt.cabocha', encoding='utf-8') as f:
        morphs, _ = read_cabocha(f)

    punct_p = lambda x: False if x in ["、", "。", "。。"] else True
    parsed = add_chunks(morphs)
    sent = parsed[7]
    visualize_dependency(sent, "../out/p44/test.dot")
    for i, sent in enumerate(parsed):
        visualize_dependency(sent, "../out/p44/sent{}.png".format(i))
        if i > 100:
            break
