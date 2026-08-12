my_list = ['three', 'four', 'eleven', 'one']
my_list.sort() 
print(my_list) # ['eleven', 'four', 'one', 'three']

my_list.sort(key=lambda string: len(string)) 
# Sorting based on the number of characters 

print(my_list) # ['one', 'four', 'three', 'eleven']