# Prime Numbers
# Create a function that returns a list of all prime numbers up to a given number.
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. For example, 2, 3, 5, 7, and 11 are prime numbers.

maximum_number = int(input("Enter the maximum number: "))   # Get the max number to evaluate
prime_numbers = ""                                          # Store the prime numbers
divisor_count = 0                                           # Store the counter of divisors for num
for number in range(2, maximum_number+1):                   # Loop through num from 2 up to max number
    divisor_count = 0                                       # Reset the number of divisible number to 0
    for divisor in range(1, number+1):                      # Loop through divisor from 1 up to the num being evaluated
        if number % divisor == 0:                           # Check if num is divisible by divisor
            divisor_count += 1                              # Count up the instances num is divisible by divisor
    if divisor_count < 3:                                   # Check if the divisibility of num is less than 3
        if prime_numbers == "":                             # Check if prime_numbers is still empty
            prime_numbers += str(number)                    # Append num only, the first value
        else:
            prime_numbers += ", " + str(number)             # Append a comma and num for succeeding values

print(f'Prime numbers: {prime_numbers}')                    # Print all the identified prime numbers