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

# Print Output
print("Modified list:", numbers_list)
print("Tuple remains unchanged:", numbers_tuple)
print("Union of set:", set_union)
print("Intersection of set:", set_intersection)
print("Difference of set:", set_difference)
print("Updated Dictionary:", numbers_dict)