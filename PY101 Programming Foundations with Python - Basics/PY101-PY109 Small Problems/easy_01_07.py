# input: Two strings. Length will differ of each string.
# output: To return single string containing short string + long string 
#         + short string again length wise.
# Test Cases:
#   print(short_long_short('abc', 'defgh') == "abcdefghabc")
#   print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
#   print(short_long_short('', 'xyz') == "xyz")
# Data Structure and Algorithm:
#   a. Intialize the shorter string and longer string as empty strings.
#   b. Compare the length of the strings. if str1 length < str2 length,
#      then shorter_string = str1  and longer_string = str2 else vice versa.
#   c. Add shorter_string + longer_string + shorter_string and return it.

def short_long_short(str1, str2):
    short = ''
    long = ''
    if len(str1) < len(str2):
        short = str1
        long = str2
    else:
        short = str2
        long = str1
    
    return short + long + short

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")