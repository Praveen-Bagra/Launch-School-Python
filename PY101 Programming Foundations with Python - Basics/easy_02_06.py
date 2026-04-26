# input: string with atleast 2 words.
# output: Return the second last word. Words are any sequence of 
#         non-blank characters. It means words are seperated by blank
#         characters. We have to return string.
# Test Cases:
#   print(penultimate("last word") == "last")
#   print(penultimate("Launch School is great!") == "is")
# Data Structure and Algorithm:
#   a. Initialize the words list = Split the string into words list.
#      str.split() 
#   b. Return the second last word from words list i.e. list[-2]

def penultimate(sentence):
    words = sentence.split()
    return words[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")