import os
import pytest
from lark_grammars import grammars
from lark import Lark
from hypothesis.extra.lark import from_lark

grammars = [(name, path) for name, path in grammars.grammar_files.items()]
skipped = ["gedcom.lark", "eqn.lark", "phone_number.lark", "pf.lark",
           "postal.lark", "python3.lark", "restructuredtext.lark",
           "rfc_822.lark", "rfc_822_datetime.lark", "rfc_1738.lark",
           "rfc_2397.lark", "rfc_2396.lark", "rfc_6531.lark",
           "rfc_5321.lark", "rfc_5545.lark", "subunit_v1.lark",
           "toml.lark", "yaml.lark"]


@pytest.mark.parametrize("name,path", grammars)
def test_grammars(name, path):
    if os.path.basename(path) in skipped:
        pytest.skip()
    with open(path, 'r') as fh:
        from_lark(Lark(fh)).example()
