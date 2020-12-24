### lark grammars

[![PyPI version](https://badge.fury.io/py/lark-grammars.svg)](https://badge.fury.io/py/lark-grammars)

Grammars suitable for [lark](https://github.com/lark-parser/lark) parser:

- [bc](https://man.openbsd.org/bc), an arbitrary precision calculator language (```bc.lark```)
- [The GEDCOM Standard](http://user.it.uu.se/~andersa/gedcom/) (```gedcom.lark```)
- [eqn](https://man.openbsd.org/eqn), language reference for mandoc (```eqn.lark```)
- [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html), Date and time format ```iso-8601.lark```)
- [mdoc](https://man.openbsd.org/mdoc.7), semantic markup language for formatting manual pages (```mdoc.lark```)
- MIME [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml) (```mime.lark```)
- Lua 5.1 language grammar specification (```lua.lark```)
- [TAP13](https://testanything.org/tap-version-13-specification.html) - The Test Anything Protocol v13 (```tap13.lark```)
- [Palindrome](https://en.wikipedia.org/wiki/Palindrome) is a word, number, or
  other sequence of characters which reads the same backward as forward, such
  as ```madam``` or ```racecar``` or the number ```10801```
  (```palindrome.lark```)
- [OpenBSD packet filter configuration file](https://man.openbsd.org/pf.conf) (```pf.lark```)
- ```phone_number.lark```
- Postal Address (```postal.lark```)
- Python 3 language grammar specification (```python3.lark```)
- [POSIX Regular Expressions](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html) (```regex.lark```)
- [reStructuredText Markup Syntax](https://docutils.sourceforge.io/rst.html) (```restructuredtext.lark```)
- [RFC 822: Standard for ARPA Internet Text Messages](https://www.ietf.org/rfc/rfc822.txt) (```rfc_822.lark```)
- [RFC 1738: Uniform Resource Locators (URL)](https://www.ietf.org/rfc/rfc1738.txt) (WIP) (```rfc_1738.lark```)
- [RFC 2396: Uniform Resource Identifiers (URI)](https://www.ietf.org/rfc/rfc2396.txt) (```rfc_2396.lark```)
- [RFC 2397: The "data" URL scheme](https://tools.ietf.org/html/rfc2397) (```rfc_2397.lark```)
- [RFC 5545: Internet Calendaring and Scheduling Core Object Specification (iCalendar)](https://tools.ietf.org/html/rfc5545) (```rfc_5545.lark```)
- [RFC 6531: SMTP Extension for Internationalized Email](https://tools.ietf.org/html/rfc6531) (WIP) (```rfc_6531.lark```)
- [RFC 5321: Simple Mail Transfer Protocol](https://tools.ietf.org/html/rfc5321) (WIP) (```rfc_5321.lark```)
- [robots.txt](http://www.robotstxt.org/robotstxt.html) (```robotstxt.lark```)
- SQLite (```sqlite.lark```)
- [SubUnit v1](https://github.com/testing-cabal/subunit) - SubUnit v1 protocol specification (```subunit_v1.lark```)
- [Tom's Obvious, Minimal Language](https://github.com/toml-lang/toml) (```toml.lark```)
- [YAML: YAML Ain't Markup Language](https://yaml.org) (```yaml.lark```)

### How-To Use:

```
$ python -m venv venv
$ python -m pytest tests/test_grammars.py
$ pip install lark_grammars
$ cat example.py
from lark_grammars import grammars                     
grammars.grammar_files['bc'] 

$ python generate.py --grammar grammars/tap13.lark
TAP version 13
1..861602252
not ok # Skipped

# - C o A 2 1 H
```

### See grammars for other parsers:

- [ANTLR v4](https://github.com/antlr/grammars-v4)
- [PEG](https://github.com/PhilippeSigaud/Pegged/wiki/Grammar-Examples)
