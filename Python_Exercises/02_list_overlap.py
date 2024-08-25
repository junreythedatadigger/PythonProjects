# List Overlap
# Write a program that returns a list containing only the common elements between two lists.
# For example, given the lists [1, 2, 3, 4] and [3, 4, 5, 6], the program should return [3, 4].

entered_list1 = input("Enter 1st list separated by comma: ").split(",")
entered_list2 = input("Enter 2nd list separated by comma: ").split(",")
# entered_list1 = [1,2,3,4,1,2,3,4]
# entered_list2 = [3,4,4,5,6,1,2,2]

# Convert each element from string to integer
entered_list1 = [int(i) for i in entered_list1]
entered_list2 = [int(i) for i in entered_list2]

# Sort the elements into ascending order
entered_list1.sort()
entered_list2.sort()

# Store the sorted lists
sorted_list1 = entered_list1
sorted_list2 = entered_list2

# Storage for the list of overlapping elements
list_overlap = []

i, j = 0, 0                                             # Initialize index counters to 0
while i < len(sorted_list1):                            # Loop through the 1st sorted list
    while j < len(sorted_list2):                        # Loop through the 2nd sorted list
        try:                                            # Try if index is out of range
            if sorted_list1[i] == sorted_list2[j]:      # Check if elements between list matches
                list_overlap.append(sorted_list1[i])    # If true then store element to list_overlap
                sorted_list1.pop(i)                     # Then remove matching element in sorted_list1
                sorted_list2.pop(j)                     # Then remove matching element in sorted_list2
            else:
                j += 1                                  # Or else increment counter for sorted_list2
        except IndexError as error:                     # If IndexError then catch and proceed
            # print(f'Error: {error}')
            break
    else:
        i += 1                                          # Increment sorted_list1 counter
        j = 0                                           # Reset to 0 sorted-list2 counter

print(f'List of common elements = {list_overlap}')      # Print all the common elements between lists