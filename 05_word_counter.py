# Word Counter
# Create a program that counts the number of words, characters, and lines in a
# given text file. This will give you experience with file I/O operations and string
# manipulation.

f = open('README.md', 'rt')
# print(f.read(2))

# contents = f.read()
# print(f'length {len(contents)}')
# print(contents)
#
print(f'1st line {f.readline()}')
print(f'2nd line {f.readline()}')

# if '\n' in contents:
#     print('yes')