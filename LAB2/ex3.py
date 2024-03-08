# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:

str_list = input_numbers.split(" ")
numbers_list = [int(i) for i in str_list]
tuple_numbers = tuple(numbers_list)

# Manipulate List
#   Append 10 to the list
numbers_list.append(10)
#   Insert 20 at index 2
#   Remove one elementfrom the list

# Attempt to Modify Tuple (this will raise an error)
try:
    #   Append 10 to the tuple
except AttributeError:
    print("Tuples are immutable and cannot be modified.")
try:
    #   Insert 20 at index 2
except AttributeError:
    pass  # Insert operation will also raise an error
try:
    #   Remove one element  from the tuple
except AttributeError:
    pass  # Remove operation will also raise an error

# Print Output
print("Modified list:", numbers_list)
print("Tuple remains unchanged:", numbers_tuple)