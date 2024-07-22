# Calculator
# Build a basic calculator that can perform operations like addition, subtraction,
# multiplication, and division. This will give you practice with functions and control
def calculate(first_num, operator, second_num):
    if operator == '*':
        return first_num * second_num
    elif operator == '/':
        return first_num / second_num
    elif operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num

first_num = int(input('Enter the first number: '))
operator = input('Enter the operator (+-*/): ')
second_num = int(input('Enter the second number: '))

result = calculate(first_num, operator, second_num)
print(f'Result: {first_num} {operator} {second_num} = {result}')