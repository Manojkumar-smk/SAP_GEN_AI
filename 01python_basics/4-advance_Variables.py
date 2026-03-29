##list

from typing import Union


my_list = ['apple', 'orange', 'mango']

print("first item:", my_list[0])
print("last item:", my_list[-1])

my_list.append('pineapple')

my_list.insert(2, 'graphes')

print(my_list)

print("Extract", my_list[1:2])

print("Extract", my_list[1:-1]) # extract n-1 record from list

print(len(my_list))

my_list.remove('orange')

my_list.pop()

#list membership chec

if 'apple' in my_list:
    print("available")

#list comprehension
my_numbers = [1, 2, 3, 4, 5]
sq_root = [x**2 for x in my_numbers]
print(sq_root)

new_list = my_list + my_numbers
print(new_list)

#tuples


numbers = (1, 2, 3, 2, 4, 2)

# .count(): How many times a value appears
print(numbers.count(2))  # Output: 3

# .index(): Find the first position of a value
print(numbers.index(4))  # Output: 4

# Joining tuples (creates a NEW tuple)
new_tuple = numbers + (30, 40) 
print(new_tuple)  # Output: (10, 20, 30, 40)

not_a_tuple = (5)   # This is just the integer 5
is_a_tuple = (5,)   # This is a tuple containing 5


my_tuple = (1,2,3,4,5)
# immutable

#sets

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Everything from both (no duplicates)
print(set_a | set_b)          # {1, 2, 3, 4, 5, 6}

# Intersection: Only items in BOTH
print(set_a & set_b)          # {3, 4}

# Difference: Items in A but NOT in B
print(set_a - set_b)          # {1, 2}

# Symmetric Difference: Items in either A or B, but NOT both
print(set_a ^ set_b)          # {1, 2, 5, 6}

#dictionary