# input: list
# output: string
# rules:
#   Explicit:
#       - Print each element(word) and the number of occurences in a list.
#       - Words are case sensitive. ('Mom' != 'mom')
# Test Cases / Examaples
#   vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            #   'motorcycle', 'motorcycle', 'car', 'truck']

#   count_occurrences(vehicles)

#   car => 4
#   truck => 3
#   SUV => 1
#   motorcycle => 2
# Data Structure and Algorithm:
#   - Initialize variable word_counts to empty dictionary.
#   - Iterate over each word in original list:
#       - If word is in word_counts:
#               increase its associated value by 1.
#       - else
#               add word and its associated value to 1 in word_counts
#   - Iterate over each word, count in words_count
#       - print word ==> count

def count_occurrences(lst):
    # word_counts = {}
    # for word in lst:
        # if word in word_counts:
            # word_counts[word] += 1
        # else:
            # word_counts[word] = 1

    # for word, count in word_counts.items():
        # print(f'{word} => {count}')
    
    unique_words = set(lst)
    for word in unique_words:
        print(f'{word} => {lst.count(word)}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)