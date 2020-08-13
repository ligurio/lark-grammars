#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from lark import Lark
from hypothesis.extra.lark import from_lark

DEFAULT_START = 'start'

_ROOT = os.path.abspath(os.path.dirname(__file__))

def _build_path(name):
    return os.path.join(_ROOT, 'grammars', name)

grammar_files = {'bc': _build_path('bc.lark'),
            'gedcom': _build_path('gedcom.lark'),
            'palindrome': _build_path('palindrome.lark'),
            'phone_number': _build_path('phone_number.lark'),
            'pf': _build_path('pf.lark'),
            'postal': _build_path('postal.lark'),
            'regex': _build_path('regex.lark'),
            'restructuredtext': _build_path('restructuredtext.lark'),
            'rfc_822': _build_path('rfc_822.lark'),
            'rfc_822_datetime': _build_path('rfc_822_datetime.lark'),
            'rfc_1738': _build_path('rfc_1738.lark'),
            'rfc_2397': _build_path('rfc_2397.lark'),
            'rfc_2396': _build_path('rfc_2396.lark'),
            'rfc_6531': _build_path('rfc_6531.lark'),
            'rfc_5321': _build_path('rfc_5321.lark'),
            'rfc_5545': _build_path('rfc_5545.lark'),
            'robotstxt': _build_path('robotstxt.lark'),
            'subunit_v1': _build_path('subunit_v1.lark'),
            'tap13': _build_path('tap13.lark'),
            'toml': _build_path('toml.lark'),
            'yaml': _build_path('yaml.lark')}

if __name__ == '__main__':
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
