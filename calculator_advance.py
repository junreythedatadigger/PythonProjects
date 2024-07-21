def calculate(first_num, operator, second_num):
	if operator == '*':
		return first_num * second_num
	elif operator == '/':
		return first_num / second_num
	elif operator == '+':
		return first_num + second_num
	elif operator == '-':
		return first_num - second_num

def evaluate(operations):
	i = 0
	while i < len(new_equation):
		# print(f'Length {len(new_equation)}, index {i}')
		if new_equation[i] in operations:
			new_equation[i - 1] = str(calculate(float(new_equation[i - 1]), new_equation[i], float(new_equation[i + 1])))
			new_equation.pop(i)  # remove the operator from the array
			new_equation.pop(i)  # remove the second number from the array
			# print(new_equation[i - 1])
			# print(new_equation)
		else:
			i += 1
	# print('Done')

equation = input('Enter equation: ')
#equation = '1+2-3+4-5'
# equation = '1-2+3/3*5-6+7/7*9'
# equation = '9*8/8+6-5*4/4+2-1'
new_equation = []
operand = ''
# print(equation)

# Separate the operands and operators
operators = '+-*/'
for i in range(len(equation)):
	# print(f'i = {i}')
	if equation[i] in operators:
		new_equation.append(operand)
		operand = ''
		new_equation.append(equation[i])
		# print(f'new_equation = {new_equation}')
	else:
		operand += equation[i]
		# print(f'operand = {operand}')
# the last operand
new_equation.append(operand)
print(new_equation)

evaluate('*/')
evaluate("+-")

print(new_equation)
print(f'Result {eval(equation)}')
