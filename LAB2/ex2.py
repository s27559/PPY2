# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:

str_list = input_numbers.split(" ")
numbers_list = [int(i) for i in str_list]
tuple_numbers = tuple(numbers_list)

# Sorting:

numbers_list.sort()
sorted_tuple = tuple(sorted(tuple_numbers))


# Print Output
print("Sorted list:", numbers_list)
print("Sorted tuple:", sorted_tuple)