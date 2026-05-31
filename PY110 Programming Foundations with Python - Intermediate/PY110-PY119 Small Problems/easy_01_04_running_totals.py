# input: list
# output: new list with same number of elements as original list
# rules:
#   Explicit:
#       - To return a new list. Each element should be the running 
#         total from the original list.
#   Implicit:
#       - Empty list should return empty list.
# Test Cases / Examples:
    # print(running_total([2, 5, 13]) == [2, 7, 20])    # True
    # print(running_total([14, 11, 7, 15, 20])
        # == [14, 25, 32, 47, 67])                    # True
    # print(running_total([3]) == [3])                  # True
    # print(running_total([]) == [])                    # True
# Data Structure/ Algorithm:
#   - Initialize variable running_total_list to empty list.
#   - Iterate over num in an original list:
#       If it is first element:
#           add first first element to running_total_list
#       else
#           add (that element + running_total_list last element)
#           to the running_total_list
#   - Return running_total_list

def running_total(nums):
    running_total_list = []
    for idx, num in enumerate(nums):
        if idx == 0:
            running_total_list.append(num)
        else:
            running_total_num = num + running_total_list[-1]
            running_total_list.append(running_total_num)

    return running_total_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True