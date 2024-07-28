# Password Generator
# Develop a password generator that creates random, secure passwords based on
# user-defined criteria (e.g., length, inclusion of special characters). This project will
# help you understand random number generation and string handling.

from random import randrange

# Define the different categories of characters
numbers = '0123456789'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_char = '`~!@#$%^&*()-_=+[{]}|;:",<.>/?'

# Set the criteria for the password to generate
password_length = int(input('Password length: '))
include_numbers = input('Include number? (y/n): ')
include_lower_letters = input('Include lower letters? (y/n): ')
include_upper_letters = input('Include upper letters? (y/n): ')
include_special_characters = input('Include special characters? (y/n): ')

# Apply the criteria specified by the user
password_characters = ''
if include_numbers == 'y':
    password_characters += numbers

if include_lower_letters == 'y':
    password_characters += lower_letters

if include_upper_letters == 'y':
    password_characters += upper_letters

if include_special_characters == 'y':
    password_characters += special_char

# Generate the password based on the specified criteria
generated_password = ''
for i in range(password_length):
    generated_password += password_characters[randrange(0,len(password_characters)-1)]

print(f'Generated password: {generated_password}')