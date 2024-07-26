# List Overlap
# Write a program that returns a list containing only the common elements between two lists.
# For example, given the lists [1, 2, 3, 4] and [3, 4, 5, 6], the program should return [3, 4].

# list1 = [1,2,3,4,6]
# list2 = [3,4,4,5,6]

list1 = input("Enter 1st list separated by comma: ").split(",")
list2 = input("Enter 2nd list separated by comma: ").split(",")
print(f'list1 = {list1}')
print(f'list2 = {list2}')
new_list = []

i, j = 0, 0
while i < len(list1):
    # print(f'len(list1)={len(list1)}')
    # print(f'i={i}')
    while j < len(list2):
        # print(f'len(list1)={len(list1)}, len(list2)={len(list2)}')
        # print(f'i={i}, j={j}')
        try:
            if list1[i] == list2[j]:
                # print(f'list1[i]={list1[i]}, list2[j]={list2[j]}')
                new_list.append(list1[i])
                list1.pop(i)
                list2.pop(j)
                # print(f'new_list={new_list}')
                # print(f'list1={list1}')
                # print(f'list2={list2}')
                # j -= 1
            else:
                j += 1
        except IndexError as error:
            # print(f'Error: {error}')
            break
    else:
        i += 1
        # if j == len(list2):
        j = 0

print(f'List overlap = {new_list}')