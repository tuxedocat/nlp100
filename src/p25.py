# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess
import gzip
import json
import re
import io

filepath = "../dat/jawiki-country.json.gz"

def extractmetadata(text):
    """Extract media [[File:<filename>...]]"""
    meta = re.compile(r"(?<=\{\{基礎情報).+?(?=\}\}\n)", re.DOTALL) # non-greedy search
    return meta.search(text)

def getpair(line):
    """Extract key, value pair from a line"""
    pair = re.compile(r"\|(?P<key>.+) = (?P<value>.+)")
    _m = pair.search(line)
    if _m:
        key = _m.group('key')
        value = _m.group('value')
        return (key, value)

if __name__ == '__main__':
    """Read JSON file, and extract Wikipedia's common metadata"""

    # For Atom's run script console...
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    j = {}
    with gzip.open(filepath, 'rb') as raw:
        for line in raw:
            _j = json.loads(line.decode("utf-8"))
            j[_j["title"]] = _j["text"]
    text = j["イギリス"]

    metadata = {}
    for line in extractmetadata(text).group().split("\n"):
        _p = getpair(line)
        if _p:
            metadata[_p[0]] = _p[1]
    for k, v in metadata.items():
        print("key={},\tvalue={}".format(k, v))
