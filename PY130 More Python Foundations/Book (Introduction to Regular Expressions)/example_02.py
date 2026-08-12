import re

strings1 = [ 
        "I love Launch School!",
        "LAUNCH SCHOOL! Gotta love it!",
        "launchschool.com",
]

# text = "1 2 3 \t 4 5 6"
# if re.search(r'\t', text):
    # print("has tab")

for string in strings1:
    if re.search('launch', string, flags=re.IGNORECASE):
        print(string)
        # I love Launch School!
        # LAUNCH SCHOOL! Gotta love it!
        # launchschool.com

    