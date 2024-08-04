# List Overlap
# Write a program that returns a list containing only the common elements between two lists.
# For example, given the lists [1, 2, 3, 4] and [3, 4, 5, 6], the program should return [3, 4].


def list_overlap_func(first_list,second_list):

    # Sort the elements into ascending order
    first_list.sort()
    second_list.sort()

    # Storage for the list of overlapping elements
    list_overlap = []

    i, j = 0, 0                                             # Initialize index counters to 0
    while i < len(first_list):                              # Loop through the first list
        while j < len(second_list):                         # Loop through the second list
            try:                                            # Try if index is out of range
                if first_list[i] == second_list[j]:         # Check if elements between list matches
                    list_overlap.append(first_list[i])      # If true then store element to list_overlap
                    first_list.pop(i)                       # Then remove matching element in first list
                    second_list.pop(j)                      # Then remove matching element in second list
                else:
                    j += 1                                  # Or else increment counter for second list
            except IndexError as error:                     # If IndexError then catch and proceed
                # print(f'Error: {error}')
                break
        else:
            i += 1                                          # Increment first list counter
            j = 0                                           # Reset to 0 second list counter

    return list_overlap

# # Convert the entered string to list separated by comma
# entered_list1 = input("Enter 1st list separated by comma: ").split(",")
# entered_list2 = input("Enter 2nd list separated by comma: ").split(",")
#
# # Convert each element from string to integer
# entered_list1 = [int(i) for i in entered_list1]
# entered_list2 = [int(i) for i in entered_list2]
#
# # entered_list1 = [1,2,3,4,1,2,3,4]
# # entered_list2 = [3,4,4,5,6,1,2,2]
#
# print(f'List of common elements = {list_overlap_func(entered_list1,entered_list2)}')      # Print all the common elements between lists