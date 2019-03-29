#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lark import Lark
from hypothesis.extra.lark import from_lark
import argparse
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate grammar samples.')
    parser.add_argument('--grammar', dest='grammar',
                        help='file with grammar syntax')
    parser.add_argument('--start', dest='start',
                        help='start terminal')
    args = parser.parse_args()
    if (not args.grammar):
	sys.exit(1)
    if args.grammar == "mime.lark":
       sys.setrecursionlimit(10000)

    with open(args.grammar, 'r') as grammar:
    	print from_lark(Lark(open(args.grammar, 'r'), start="start")).example()
