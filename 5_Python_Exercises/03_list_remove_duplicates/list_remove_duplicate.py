# List Remove Duplicates
# Write a function that removes duplicates from a list.
# For example, given the list [1, 2, 2, 3, 4, 4, 5], the function should return [1, 2, 3, 4, 5].

def list_remove_duplicate_func(list):

    # Store the list without duplicates
    new_list = []

    for i in list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    new_list.sort()
    return new_list


# # Convert a string to list separated by comma
# entered_list = list(input("Enter a list of numbers separated by comma: ").split(","))
#
# # Convert each number into integer type
# entered_list = [int(i) for i in entered_list]
#
# # Sort converted list into ascending order
# entered_list.sort()
#
# # print(f'Sorted list in ascending order = {entered_list}')
#
# print(f'Removed duplicates in the list = {list_remove_duplicate_func(entered_list)}')