def get_common_prefix(first_word, second_word):
    common_pref = ""
    if len(first_word) < len(second_word):
        short_word = first_word
        long_word = second_word
    else:
        short_word = second_word
        long_word = first_word

    for i in range(len(long_word)):
        if short_word[i] == long_word[i]:
            common_pref += short_word[i]
        else:
            return common_pref