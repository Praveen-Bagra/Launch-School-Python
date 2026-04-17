def starts_with(sentence, substring):
    return sentence.startswith(substring)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True