# Fibonacci Sequence
# Write a function that generates the first 10 numbers in the Fibonacci sequence.
# The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones, starting from 0 and 1.
# For example, the first 10 numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

limit = 10
fibonacci_sequence_list = [0,1]
while len(fibonacci_sequence_list) < limit:
    fibonacci_sequence_list.append(fibonacci_sequence_list[-2]+fibonacci_sequence_list[-1])
fibonacci_sequence = ", ".join(str(item) for item in fibonacci_sequence_list)
print(f'Fibonacci Sequence of the first {limit} numbers are: {fibonacci_sequence}')