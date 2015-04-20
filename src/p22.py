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

filepath = "../dat/jawiki-country.json.gz"

def searchcat(text):
    """Extract name of category by lookahead, and lookbehind"""
    cat = re.compile(r"(?<=\[\[Category:).*(?=\]\])")
    return cat.findall(text)

if __name__ == '__main__':
    """Read JSON file, and print the article about the UK"""
    j = {}
    with gzip.open(filepath, 'rb') as raw:
        for line in raw:
            _j = json.loads(line.decode("utf-8"))
            j[_j["title"]] = _j["text"]
    text = j["イギリス"]
    print(searchcat(text))
