#!/bin/python

import sys
import argparse

parser = argparse.ArgumentParser(description="phrase table gen")
parser.add_argument("--freq", "-f", type=str, default="freq/phrase.txt")
parser.add_argument("--code", "-c", type=str, default="table/yi_fullcode_table.txt")
parser.add_argument("--table", "-t", type=str, default="table/yi_table.txt")
args = parser.parse_args()

fullcode_map: dict[str, str] = {}
simpcode_map: dict[str, str] = {}

phrasecode_map: dict[str, str] = {}
deferred_list: list[tuple[str, str]] = []

with open(args.code) as fullcode_list:
    for line in fullcode_list.readlines():
        [char, fullcode] = line.strip(" \t\n\r").split('\t')
        fullcode_map[char] = fullcode

with open(args.table) as code_list:
    for line in code_list.readlines():
        [char, code, _] = line.strip(" \t\n\r").split('\t')
        simpcode_map[char] = code

def add_phrase(phrase: str, fullcode: str) -> str:
    for i in range(4, len(fullcode)):
        if not phrasecode_map.get(fullcode[:i]):
            phrasecode_map[fullcode[:i]] = phrase
            return fullcode[:2]+';'+fullcode[2:i]
    return fullcode[:2]+';'+fullcode[2:]

with open(args.freq) as freq_list:
    for line in freq_list.readlines():
        [phrase, freq] = line.strip(" \t\n\r").split('\t')

        match len(phrase):
            case 0|1:
                print("WARN:", phrase, file=sys.stderr)
                continue

            case 2:
                first, second = simpcode_map.get(phrase[0]), simpcode_map.get(phrase[1])
                if not first or not second:
                    print("ERROR:", phrase, file=sys.stderr)
                    continue
                if len(first) + len(second) < 6:
                    deferred_list.append((phrase, freq))
                    continue
                first, second = fullcode_map[phrase[0]], fullcode_map[phrase[1]]
                print("%s\t%s\t%s" % (phrase, add_phrase(phrase, first[:2]+second), freq))

            case _:
                first, second, last = simpcode_map.get(phrase[0]), simpcode_map.get(phrase[1]), simpcode_map.get(phrase[-1])
                if not first or not second or not last:
                    print("ERROR:", phrase, file=sys.stderr)
                    continue
                if len(first) + len(second) + len(last) <= 6:
                    deferred_list.append((phrase, freq))
                    continue
                first, second, last = fullcode_map[phrase[0]], fullcode_map[phrase[1]], fullcode_map[phrase[-1]]
                print("%s\t%s\t%s" % (phrase, add_phrase(phrase, first[0]+second[0]+last), freq))

    for phrase, freq in deferred_list:
        match len(phrase):
            case 2:
                first, second = fullcode_map[phrase[0]], fullcode_map[phrase[1]]
                print("%s\t%s\t%s" % (phrase, add_phrase(phrase, first[:2]+second), freq))
            case _:
                first, second, last = fullcode_map[phrase[0]], fullcode_map[phrase[1]], fullcode_map[phrase[-1]]
                print("%s\t%s\t%s" % (phrase, add_phrase(phrase, first[0]+second[0]+last), freq))

