def is_anagram(first_string: str, second_string: str):
    first_array, second_array = [], []
    for i in first_string.lower():
        if i.isalnum():
            first_array.append(i)

    for i in second_string.lower():
        if i.isalnum():
            second_array.append(i)

    first_array.sort()
    second_array.sort()

    if first_array == second_array:
        return True
    else:
        return False


print(is_anagram("123", "132"))

