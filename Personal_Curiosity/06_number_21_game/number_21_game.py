def select_order(choice):
    if choice == 1:
        return "You"
    elif choice == 2:
        return "Computer"
    else:
        return "Incorrect choice!"


def enter_numbers(last_number, numbers):
    number_list = numbers.split(",")
    try:
        number_list = [int(i) for i in number_list]
        if len(number_list) < 4:
            if number_list[0] == last_number + 1:
                for i in range(len(number_list)-1):
                    if number_list[i]+1 == number_list[i+1]:
                        pass
                    else:
                        return "Numbers not in sequence"
                return number_list
            else:
                return f"Should start at {last_number+1}"
        else:
            return "Numbers exceeds 3 inputs"
    except:
        return "Invalid inputs"


def computers_turn(last_number, no_of_inputs):
    number_list = []
    for i in range(1, no_of_inputs+1):
        number_list.append(last_number+i)
    return number_list


def main():
    number_21_list = []
    choice = int(input("Enter your choice: "))
    print(select_order(choice))
    while len(number_21_list) < 21:


if __name__ == "__main__":
    main()