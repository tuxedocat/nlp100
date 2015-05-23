# -*- coding: utf-8 -*-

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__license__ = "MIT"
from itertools import takewhile
import json
import pydot


punct_p = lambda x: False if x in ["、", "。"] else True


class PrinterMixin:

    def __init__(self):
        self.parsed = None

    def printmorph(self):
        print("suf: {suf}\tpos: {pos}\tpos1: {pos1}\tbase: {base}".format(
            suf=self.surface, pos=self.pos, pos1=self.pos1, base=self.base))

    def printchunk(self):
        for m in self.morphs:
            m.printmorph()
        print("src: {src}\tdepto: {dep2}".format(
            src=self.srcs, dep2=self.dst))


class ExtractMixin:

    def chunktext(self, filter_p=None, sep=""):
        return sep.join(filter(filter_p, [m.surface for m in self.morphs]))

    def chunktext_vbase(self, filter_p=None, sep=""):
        return sep.join(filter(filter_p, [m.base for m in self.morphs]))

    def chunkpos(self, filter_p=None, sep=""):
        return sep.join(filter(filter_p, [m.pos for m in self.morphs]))

    def _vbase(self, m=None):
        return m.base if m.pos == "動詞" else m.surface

    def chunktext_with_jsonmetadata(self, chunkidx=None):
        return "".join([m.surface for m in self.morphs])

    def _get_jsonmetadata_for_morph(self, m=None, idx=None):
        d = {"suf": m.surface, "pos": m.pos,
             "pos1": m.pos1, "base": m.base, "chunkid": idx}
        return json.dumps(d)

    def _get_jsonmetadata_for_chunk(self, c=None, idx=None):
        d = {"suf": c.chunktext(sep="/"), "pos": c.chunkpos(sep="/"),
             "base": c.chunktext_vbase(sep="/"), "chunkid": c.srcs[0] if c.srcs else None, "to": c.dst}
        return json.dumps(d)


class Morph(PrinterMixin):

    def __init__(self, raw):
        self.raw = raw
        try:
            self._parseline()
        except (IndexError, AttributeError):
            self.surface = ""
            self.base = ""
            self.pos = ""
            self.pos1 = ""

    def _parseline(self):
        _ = self.raw.strip().split("\t")
        _m = _[1].split(",")
        self.surface = _[0]
        self.base = _m[6]
        self.pos = _m[0]
        self.pos1 = _m[1]


class Chunk(PrinterMixin, ExtractMixin):

    def __init__(self, morphlist, meta):
        self.morphs = morphlist
        self.meta = meta
        self._setdeps()

    def _setdeps(self):
        _ = self.meta.strip().split()
        self.srcs = [int(_[1])]
        self.dst = int("".join([c for c in _[2] if c.isdigit() or c == "-"]))


def read_cabocha(file):
    """
    args:
        file: file like object (plain text, cabocha's -f1 format)
    returns:
        parsed: List[List[Morph|String]]
        metadata: List[List[string]]
    """
    morphs = []
    metadata = []
    _s = []
    _m = []
    for line in file:
        if line.startswith("EOS"):
            morphs.append(_s)
            _s = []
            metadata.append(_m)
            _m = []
        elif line.startswith("*"):
            _m.append(line)
            _s.append(line)
        else:
            _s.append(Morph(line))
    return (morphs, metadata)


def add_chunks(morphs):
    """
    args:
        morphs: List[List[Morph, or String]], given by read_cabocha
    returns:
        parsed: List[List[Chunk]]
    """
    parsed = []
    _s = []
    _m = None  # metadata
    _c = []  # sublist of chunks
    p = lambda x: isinstance(x, Morph)
    for sentence in morphs:
        while sentence:
            m = sentence.pop(0)
            if isinstance(m, str):
                _m = m
                _s = list(takewhile(p, sentence))
                _c.append(Chunk(_s, _m))
            else:
                pass
        parsed.append(_c)
        _c = []
    return parsed


def get_is_xx_in_chunk_func(pos=""):
    def is_xx_in_chunk(chunk_or_morphs):
        try:
            return any([m.pos == pos for m in chunk_or_morphs.morphs])
        except AttributeError:
            return any([m.pos == pos for m in chunk_or_morphs])
    return is_xx_in_chunk


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


def get_leftmostxx_func(pos, ifnone=None):
    def get_xx(morphs):
        for morph in morphs:
            if morph.pos == pos:
                return morph.base
        return ifnone

    return get_xx
