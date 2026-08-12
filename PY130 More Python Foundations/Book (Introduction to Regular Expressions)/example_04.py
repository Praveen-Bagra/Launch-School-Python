import re

# def p(text):
    # print(re.findall(r'^c.t', text, flags=re.IGNORECASE))


def p(text):
    print(re.findall(r'c.t$', text, flags=re.IGNORECASE))

p("cat")
p("cot\n")
p("CATASTROPHE")
p("WILDCAUGHT")
p("wildcat\n")
p("-CET-")
p("Yacht")