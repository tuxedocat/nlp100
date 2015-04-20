# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import subprocess
from docopt import docopt
import gzip
import json
from collections import Counter

filepath = "../dat/jawiki-country.json.gz"

if __name__ == '__main__':
    """Read JSON file, and print the article about the UK"""
    j = {}
    with gzip.open(filepath, 'rb') as raw:
        for line in raw:
            _j = json.loads(line.decode("utf-8"))
            j[_j["title"]] = _j["text"]
    print(j["イギリス"])
    with open("uk.txt", 'w') as f:
        f.write(j["イギリス"])
