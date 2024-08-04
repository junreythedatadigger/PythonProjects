def gcf_func(first_number,second_number):
    if first_number < second_number:
        lesser_number = first_number
        greater_number = second_number
    else:
        lesser_number = second_number
        greater_number = first_number

    for i in range(0, lesser_number+1):
        if lesser_number % (lesser_number - i) == 0 and greater_number % (lesser_number - i) == 0:
            return lesser_number - i