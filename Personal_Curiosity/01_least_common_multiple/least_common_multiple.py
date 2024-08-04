def lcm_func(first_number, second_number):
    if first_number < second_number:
        lesser_number = first_number
        greater_number = second_number
    else:
        lesser_number = second_number
        greater_number = first_number

    for i in range(1, greater_number+1):
        if (lesser_number*i)%greater_number == 0:
            return lesser_number*i