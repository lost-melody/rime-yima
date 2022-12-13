#!/bin/python

import argparse

parser = argparse.ArgumentParser(description="fullcode gen")
parser.add_argument("--mapping", "-m", type=str, default="table/yi_components_mapping.txt")
parser.add_argument("--spelling", "-s", type=str, default="table/yi_spelling.txt")
args = parser.parse_args()

comp_map: dict[str, str] = {}

with open(args.mapping) as mapping_list:
    for line in mapping_list.readlines():
        [comp, code] = line.strip(" \t\n\r").split('\t')
        comp_map[comp] = code

with open(args.spelling) as spelling_list:
    for line in spelling_list.readlines():
        [char, spelling] = line.strip(" \t\n\r").split('\t')
        code = list(map(lambda comp: comp_map[comp], spelling))
        print("%s\t%s" % (char, "".join(code)))

