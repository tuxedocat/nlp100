# -*- coding: utf-8 -*-

"""nlp100 in python3"""

__author__ = "Yu Sawai (tuxedocat@github.com)"
__copyright__ = "Copyright 2015, tuxedocat"
__credits__ = ["Naoaki Okazaki", "Inui-Okazaki Lab. at Tohoku University"]
__license__ = "MIT"


import sys
import gzip
import json
import re
import io
import urllib.parse
import urllib.request

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
        _v = rm_emphasis(_m.group('value'))
        _v = rm_internallink(_v)
        _v = rm_externallink(_v)
        _v = rm_htmltags(_v)
        return (key, _v)

def rm_emphasis(string):
    """remove wikimedia markup of emphasis"""
    emp = re.compile(r"'{2,5}")
    return emp.sub("", string)

def rm_internallink(string):
    """remove wikimedia markup of [[InternalLink|text]]"""
    intl = re.compile(r"\[{2}|\]{2}")
    return intl.sub("", string)

def rm_externallink(string):
    """remove wikimedia markup of [http://externallink.com]"""
    extl = re.compile(r"\[{1}http:.+?\]{1}")
    return extl.sub("", string)

def rm_htmltags(string):
    htmltags = re.compile(r"\<(|\/).+?\>")
    return htmltags.sub("", string)

def get_flagURL(flagfilename):
    q = {}
    q['titles'] = "Image:{}".format(flagfilename)
    q['prop'] = 'imageinfo'
    q['action'] = 'query'
    q['format'] = 'json'
    q['iiprop'] = 'url'
    url = "http://en.wikipedia.org/w/api.php?"
    url_val = urllib.parse.urlencode(q)
    full_url = url + url_val
    dat = urllib.request.urlopen(full_url)
    rawjson = dat.read()
    js = json.loads(rawjson.decode('utf-8'))
    return js['query']['pages'].popitem()[1]['imageinfo'][0]['url']



if __name__ == '__main__':
    """Read JSON file, and extract Wikipedia's common metadata
       And finally shows the url of the flag of the UK
    """

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

    print("The URL of the Flag of the UK:\n{}".format(get_flagURL(metadata['国旗画像'])))
