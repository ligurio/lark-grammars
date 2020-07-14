#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lark import Lark
from hypothesis.extra.lark import from_lark
import argparse
import sys
import os

module_path = os.path.dirname(__file__)

grammars = {'bc': sys.path.join(module_path, 'bc.lark'),
            'gedcom': sys.path.join(module_path, 'gedcom.lark'),
            'palindrome': sys.path.join(module_path, 'palindrome.lark'),
            'phone_number': sys.path.join(module_path, 'phone_number.lark'),
            'pf': sys.path.join(module_path, 'pf.lark'),
            'postal': sys.path.join(module_path, 'postal.lark'),
            'regex': sys.path.join(module_path, 'regex.lark'),
            'restructuredtext':
                sys.path.join(module_path, 'restructuredtext.lark'),
            'rfc_822': sys.path.join(module_path, 'rfc_822.lark'),
            'rfc_822_datetime':
                sys.path.join(module_path, 'rfc_822_datetime.lark'),
            'rfc_1738': sys.path.join(module_path, 'rfc_1738.lark'),
            'rfc_2397': sys.path.join(module_path, 'rfc_2397.lark'),
            'rfc_2396': sys.path.join(module_path, 'rfc_2396.lark'),
            'rfc_6531': sys.path.join(module_path, 'rfc_6531.lark'),
            'rfc_5321': sys.path.join(module_path, 'rfc_5321.lark'),
            'rfc_5545': sys.path.join(module_path, 'rfc_5545.lark'),
            'robotstxt': sys.path.join(module_path, 'robotstxt.lark'),
            'subunit_v1': sys.path.join(module_path, 'subunit_v1.lark'),
            'tap13': sys.path.join(module_path, 'tap13.lark'),
            'toml': sys.path.join(module_path, 'toml.lark'),
            'yaml': sys.path.join(module_path, 'yaml.lark')}

if __name__ == '__main__':
    DEFAULT_START = 'start'

    parser = argparse.ArgumentParser(description='Generate grammar samples.')
    parser.add_argument('--grammar', dest='grammar',
                        help='file with grammar syntax')
    parser.add_argument('--start', dest=DEFAULT_START,
                        help='start terminal')
    args = parser.parse_args()
    if (not args.grammar):
        sys.exit(1)
    if args.grammar == "mime.lark":
        sys.setrecursionlimit(10000)

    with open(args.grammar, 'r') as grammar:
        sample = from_lark(Lark(grammar, start=DEFAULT_START)).example()
        print('{}'.format(sample))
