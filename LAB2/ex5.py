# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:

str_list = input_numbers.split(" ")
numbers_list = [int(i) for i in str_list]
numbers_tuple = tuple(numbers_list)

# Manipulate List
#   Append 10 to the list
numbers_list.append(10)
#   Insert 20 at index 2
numbers_list.insert(2, 20)
# Remove the element 8
if 8 in numbers_list:
    numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
set1 = {0}
set1.clear()
for i in range(0,int((len(numbers_list)/2)+1)):
    set1.add(numbers_list[i])
set2 = {0}
set2.clear()
for i in range(int(len(numbers_list)/2), len(numbers_list)):
    set2.add(numbers_list[i])
# Union
set_union = set1.union(set2)
# Intersection
set_intersection = set1.intersection(set2)
# Difference
set_difference = set1.difference(set2)

# Dictionary Operations
numbers_dict = { 0:0 }
numbers_dict.clear()
for i in range(len(numbers_list)):
    numbers_dict.update({numbers_list[i]: numbers_list[i]*2})
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
numbers_dict.update({12: 32})
# Delete an existing key-value pair
numbers_dict.pop(numbers_list[1])

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = dict()
for i in range(len(numbers_list)):
    list_to_dict.update({numbers_list[i]: numbers_list[i]})
    
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = dict()
for i in range(len(numbers_tuple)):
    tuple_to_dict.update({numbers_tuple[i]: numbers_tuple[i]})
    
set_to_list = list(set_union)
set_to_tuple = tuple(set_union)
set_to_dict = dict()
for i in set_union:
    set_to_dict.update({i: i})

dict_to_list = list(numbers_dict)
dict_to_tuple = tuple(numbers_dict)
dict_to_set = set(numbers_dict)

# Print Output
print("List to Tuple:", list_to_tuple)
print("List to Set:", list_to_set)
print("List to Dictionary:", list_to_dict)
print("Tuple to List:", tuple_to_list)
print("Tuple to Set:", tuple_to_set)
print("Tuple to Dictionary:", tuple_to_dict)
print("Set to List:", set_to_list)
print("Set to Tuple:", set_to_tuple)
print("Set to Dictionary:", set_to_dict)
print("Dictionary to List:", dict_to_list)
print("Dictionary to Tuple:", dict_to_tuple)
print("Dictionary to Set:", dict_to_set)