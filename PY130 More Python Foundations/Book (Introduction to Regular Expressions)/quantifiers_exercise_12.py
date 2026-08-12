import re

strings = [
    "<h1>Main Heading</h1>",
    "<h1>Another Main Heading</h1>",
    "<h1>ABC</h1> <p>Paragraph</p> <h1>DEF</h1><p>Done</p>",
]

for string in strings:
    print(re.findall('<h1>.*?</h1>', string))