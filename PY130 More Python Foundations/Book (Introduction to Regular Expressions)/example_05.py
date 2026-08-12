import re

def p(regex, text):
    print(re.findall(regex,
                     text,
                     flags=re.IGNORECASE | re.MULTILINE))

text = ("cat\ncot\nCATASTROPHE\nWILDCAUGHT\n" +
        "wildcat\n-GET-\nYacht")

p(r'^c.t', text)
p(r'c.t$', text)