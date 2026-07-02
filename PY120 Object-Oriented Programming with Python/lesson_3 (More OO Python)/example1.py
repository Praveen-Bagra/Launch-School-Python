# str1 = 'something'
# str2 = 'something'
# print(str1 == str2)

# int1 = 1
# int2 = 1
# print(int1 == int2)

# list1 = [1, 2, 3, 'a', 'b', 'c']
# list2 = [1, 2, 3, 'a', 'b', 'c']
# print(list1 == list2)

# set1 = {1, 2, 3, 'a', 'b', 'c'}
# set2 = {'a', 1, 'c', 3, 2, 'b'}
# print(set1 == set2)

# print(str1.__class__.__name__)
# print(str2.__class__.__name__)

# str1 = 'something'
# str2 = 'something else'
# print(str1 == str2)

str1 = 'something'
str2 = ''.join(['some', 'thing'])
str3 = str1

# comparing string values
# print(str1 == str2)
# print(str1 == str3)
# print(str2 == str3)

# comparing string identity
# print(str1 is str2)
# print(str1 is str3)
# print(str2 is str3)

# num1 = 1
# num2 = 1.0

# print(num1.__class__.__name__)
# print(num2.__class__.__name__)
# print(num1 == num2)

# str1 = 'something'
# str2 = 'something'
# print(str1 is str2)

# int1 = 5
# int2 = 3 + 2
# print(int1 is int2)

# class Person:
    # def __eq__(self, other):
        # if not isinstance(other, Person)
            # return NotImplemented

        # return self.name == other.name

    # def __ne__(self, other):
        # if not isinstance(other, Person):
            # return NotImplemented

        # return self.name != other.name

# bob = Person()
# bob.name = 'bob'

# bob2 = Person()
# bob2.name = 'bob'

# print(bob == bob2)

# my_int = 45
# my_float = 45.00
# print(my_int.__eq__(my_float))
# print(my_float.__eq__(my_int))
# print(my_int == my_float)

# my_str = 'hello'
# my_int = 42
# print(my_str.__eq__(my_int))
# print(my_int.__eq__(my_str))
# print(my_str == my_int)

# class Person:
    # pass

# person1 = Person()
# person2 = Person()
# person3 = person2

# print(hex(id(person1)))
# print(hex(id(person2)))
# print(hex(id(person3)))
# print(person3 is person2)

# my_str = 'hello!'
# print(hex(id(my_str)))

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list2

# print(hex(id(list1)))
# print(hex(id(list2)))
# print(hex(id(list3)))
# print(list3 is list2)
# print(list3 is list1)

tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(hex(id(tup1)))
print(hex(id(tup2)))
print(tup1 is tup2)
