# Write a function to reverse a string.

def reverse_string(original_string):
    reversed_string = ""
    for i in range(len(original_string)):
        reversed_string += original_string[-(i+1)]
    return reversed_string

# original_string = "Hello world, hello Philippines!!"
original_string = input("Enter the string: ")
print(f'Re-versed string: {reverse_string(original_string)}')