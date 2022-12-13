#!/bin/python

import sys

trie: dict[str, dict] = {}
duplicated: dict[str, bool] = {}

def insert(spelling: str) -> bool:
    t: dict[str, dict] = trie
    is_dup: bool = True

    for c in spelling:
        if not t.get(c):
            t[c] = {}
            is_dup = False
        t = t[c]

    return is_dup


def readfile(path: str):
    with open(path) as table:
        for line in table.readlines():
            spelling = line.strip().split('\t')[1]
            if insert(spelling):
                duplicated[spelling] = True


def traverse(pre: str, t: dict[str, dict]):
    for c in t:
        if len(t[c]) == 0:
            if not duplicated.get(pre + c):
                print("%s\t%s" % ('　', pre + c))
        else:
            traverse(pre + c, t[c])


for path in sys.argv[1:]:
    readfile(path)
traverse('', trie)

