# input: string
# output: list
# rules:
#   Eplicit:
#       - Return a list containing all palindromic substrings of a
#         string.
#       - palindromic substring means it reads the same forward
#         and backward.
#       - It should be sorted by their order of appearance in the
#         input string.
#       - Duplicate substrings should be included multiple times.
#       - Use the substrings function from the previous exercise.
#       - palindrome strings are case sensitive. 'AbcbA' is a
#         palindrome, but 'Abcba' and 'Abc-bA' are not.
#       - A single character is not a palindrome.
# Test Cases / Examples:
#   print(palindromes('abcd') == [])                  # True
#   print(palindromes('madam') == ['madam', 'ada'])   # True

#   print(palindromes('hello-madam-did-madam-goodbye') ==
                  # [
                      # 'll', '-madam-', '-madam-did-madam-',
                      # 'madam', 'madam-did-madam', 'ada',
                      # 'adam-did-mada', 'dam-did-mad',
                      # 'am-did-ma', 'm-did-m', '-did-',
                      # 'did', '-madam-', 'madam', 'ada', 'oo',
                  # ])    # True

#   print(palindromes('knitting cassettes') ==
                  # [
                      # 'nittin', 'itti', 'tt', 'ss',
                      # 'settes', 'ette', 'tt',
                  # ])    # True
# Data Structure and Algorithm:
#   - Initialize palindrome_substrings = []
#   - Initialize over each substring in original string
#       - If length of substring is greater than one and substring is
#         palindrome
#               add substring to palindrome_substrings
#   - Return palindrome_substrings list.

def substrings(string):
    sub_strings = []
    start_idx = 0
    while start_idx < len(string):
        end_idx = start_idx + 1
        while end_idx <= len(string):
            sub_strings.append(string[start_idx:end_idx])
            end_idx += 1
        start_idx += 1
    
    return sub_strings

def is_palindrome(string):
    return string == string[::-1]

def palindromes(string):
    #   palindrome_substrings = []
    #   for substring in substrings(string):
        #   if len(substring) > 1 and is_palindrome(substring):
            #   palindrome_substrings.append(substring)
    
    #   return palindrome_substrings

    return [substring for substring in substrings(string)
                      if len(substring) > 1 and is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True