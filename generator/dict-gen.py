#!/bin/python

import argparse

parser = argparse.ArgumentParser(description="dict gen")
parser.add_argument("--table", "-t", type=str, default="table/yi_table.txt")
args = parser.parse_args()

simpcode_map: dict[str, str] = {}

def get_simp(char: str, fullcode: str) -> str:
    for i in range(2, len(fullcode)):
        if not simpcode_map.get(fullcode[:i]):
            simpcode_map[fullcode[:i]] = char
            return fullcode[:i]
    return fullcode

with open(args.table) as table:
    for line in table.readlines():
        [char, code, freq] = line.strip(" \t\n\r").split('\t')
        if not simpcode_map.get(code):
            simpcode_map[code] = char
            print("%s\t%s\t%s" %(char, code, freq))
        else:
            print("%s\t%s$\t%s" %(char, code, freq))

