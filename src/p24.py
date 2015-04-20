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

def searchmedia(line):
    """Extract media [[File:<filename>...]]"""
    media = re.compile(r"(?<=\[\[File:).+?\.[A-Za-z]{3}")
    return media.search(line)

if __name__ == '__main__':
    """Read JSON file, and print the article about the UK"""
    j = {}
    with gzip.open(filepath, 'rb') as raw:
        for line in raw:
            _j = json.loads(line.decode("utf-8"))
            j[_j["title"]] = _j["text"]
    text = j["イギリス"]
    
    for m in (searchmedia(line) for line in text.split("\n")):
        if m:
            print(m.group())
