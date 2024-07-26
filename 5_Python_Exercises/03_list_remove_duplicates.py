# List Remove Duplicates
# Write a function that removes duplicates from a list.
# For example, given the list [1, 2, 2, 3, 4, 4, 5], the function should return [1, 2, 3, 4, 5].

entered_list = list(input("Enter a list of numbers separated by comma: ").split(","))

# Convert each number into integer type
converted_list = []
for i in entered_list:
    converted_list.append(int(i))

# Sort converted list into ascending order
converted_list.sort()
print(f'Sorted list in ascending order = {converted_list}')

# Store the list without duplicates
new_list = []

for i in converted_list:
    if i in new_list:
        pass
    else:
        new_list.append(i)

print(f'Removed duplicates in the list = {new_list}')