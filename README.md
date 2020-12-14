### lark grammars

[![PyPI version](https://badge.fury.io/py/lark-grammars.svg)](https://badge.fury.io/py/lark-grammars)

Grammars suitable for [lark](https://github.com/lark-parser/lark) parser:

- ```mime.lark```: MIME [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)
- ```palindrome.lark```: [palindrome](https://en.wikipedia.org/wiki/Palindrome) is a word, number, or other sequence of characters which reads the same backward as forward, such as ```madam``` or ```racecar``` or the number ```10801```.
- ```tap13.lark```: [TAP13](https://testanything.org/tap-version-13-specification.html) - The Test Anything Protocol v13
- ```subunit_v1.lark```: [SubUnit v1](https://github.com/testing-cabal/subunit) - SubUnit v1 protocol
- ```bc.lark```: [bc](https://man.openbsd.org/bc), an arbitrary precision calculator language
- ```robotstxt.lark```: [robots.txt](http://www.robotstxt.org/robotstxt.html)
- ```pf.lark```: [OpenBSD packet filter configuration file](https://man.openbsd.org/pf.conf)
- ```python3.lark```: Python 3 language grammar specification
- ```regex.lark```: [POSIX Regular Expressions](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html)
- ```rfc_822.lark```: [RFC 822: Standard for ARPA Internet Text Messages](https://www.ietf.org/rfc/rfc822.txt)
- ```rfc_1738.lark```: [RFC 1738: Uniform Resource Locators (URL)](https://www.ietf.org/rfc/rfc1738.txt) (WIP)
- ```rfc_2396.lark```: [RFC 2396: Uniform Resource Identifiers (URI)](https://www.ietf.org/rfc/rfc2396.txt)
- ```rfc_2397.lark```: [RFC 2397: The "data" URL scheme](https://tools.ietf.org/html/rfc2397)
- ```rfc_5545.lark```: [RFC 5545: Internet Calendaring and Scheduling Core Object Specification (iCalendar)](https://tools.ietf.org/html/rfc5545)
- ```rfc_6531.lark```: [RFC 6531: SMTP Extension for Internationalized Email](https://tools.ietf.org/html/rfc6531) (WIP)
- ```rfc_5321.lark```: [RFC 5321: Simple Mail Transfer Protocol](https://tools.ietf.org/html/rfc5321) (WIP)
- ```toml.lark```: [Tom's Obvious, Minimal Language](https://github.com/toml-lang/toml)
- ```yaml.lark```: [YAML: YAML Ain't Markup Language](https://yaml.org)
- ```restructuredtext.lark```
- ```sqlite.lark```
- ```gedcom.lark```
- ```postal.lark```
- ```phone_number.lark```

### How-To Use:

```
$ python3 -m venv venv
$ pip3 install lark_grammars
$ cat example.py
from lark_grammars import grammars                     
grammars.grammar_files['bc'] 

$ python3 generate.py --grammar grammars/tap13.lark
TAP version 13
1..861602252
not ok # Skipped

# - C o A 2 1 H
```

### See grammars for other parsers:

- [ANTLR v4](https://github.com/antlr/grammars-v4)
- [PEG](https://github.com/PhilippeSigaud/Pegged/wiki/Grammar-Examples)
