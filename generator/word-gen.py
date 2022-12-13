#!/bin/python

import sys
import argparse

parser = argparse.ArgumentParser(description="fullcode gen")
parser.add_argument("--freq", "-f", type=str, default="freq/word.txt")
parser.add_argument("--code", "-c", type=str, default="table/yi_fullcode_table.txt")
args = parser.parse_args()

fullcode_map: dict[str, str] = {}
simpcode_map: dict[str, str] = {}

def get_simp(char: str, fullcode: str) -> str:
    for i in range(2, len(fullcode)):
        if not simpcode_map.get(fullcode[:i]):
            simpcode_map[fullcode[:i]] = char
            return fullcode[:i]
    return fullcode

with open(args.code) as fullcode_list:
    for line in fullcode_list.readlines():
        [char, fullcode] = line.strip(" \t\n\r").split('\t')
        fullcode_map[char] = fullcode

with open(args.freq) as freq_list:
    for line in freq_list.readlines():
        [char, freq] = line.strip(" \t\n\r").split('\t')

        fullcode = fullcode_map.get(char)
        if not fullcode:
            print("ERROR:", char, file=sys.stderr)
        else:
            print("%s\t%s\t%s" % (char, get_simp(char, fullcode), freq))

