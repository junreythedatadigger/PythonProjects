# Palindrome Checker
# Write a function that checks if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward (ignoring spaces, punctuation,
# and capitalization). For example, "radar" and "level" are palindromes.

entered_expression = input("Enter a word or phrase: ")
filtered_expression = "".join(character for character in entered_expression if character.isalnum()).lower()
reversed_expression = filtered_expression[::-1]
if reversed_expression == filtered_expression:
    print(f'The expression "{entered_expression}" is a palindrome.')
else:
    print(f'The expression "{entered_expression}" is not a palindrome.')
