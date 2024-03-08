# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input:

numbers_list = input_numbers.split(" ")
tuple_numbers = eval(input_numbers)

# Sorting:

numbers_list.sort()
sorted_tuple = tuple(sorted(tuple_numbers))


# Print Output
print("Sorted list:", numbers_list)
print("Sorted tuple:", sorted_tuple)