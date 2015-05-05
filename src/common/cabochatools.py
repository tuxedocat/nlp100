# -*- coding: utf-8 -*-

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__license__ = "MIT"
from itertools import takewhile


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


class Chunk(PrinterMixin):

    def __init__(self, morphlist, meta):
        self.morphs = morphlist
        self.meta = meta
        self._setdeps()

    def _setdeps(self):
        _ = self.meta.strip().split()
        self.srcs = [int(_[1])]
        self.dst = int("".join([c for c in _[2] if c.isdigit()]))


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
