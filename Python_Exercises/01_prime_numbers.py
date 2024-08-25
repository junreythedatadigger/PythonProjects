# Prime Numbers
# Create a function that returns a list of all prime numbers up to a given number.
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. For example, 2, 3, 5, 7, and 11 are prime numbers.

maximum_number = int(input("Enter the maximum number: "))   # Get the max number to evaluate
prime_numbers = ""                                          # Store the prime numbers
divisor_count = 0                                           # Counter of the divisors for number
for number in range(2, maximum_number+1):                   # Loop through num from 2 up to max number
    divisor_count = 0                                       # Reset the number of divisible number to 0
    for divisor in range(1, number+1):                      # Loop through divisor from 1 up to the number being evaluated
        if number % divisor == 0:                           # Check if number is divisible by divisor
            divisor_count += 1                              # If true then count up the instances number is divisible by divisor
    if divisor_count < 3:                                   # Check if the divisibility of number is less than 3. This is a prime number.
        if prime_numbers == "":                             # Check if prime_numbers is still empty
            prime_numbers += str(number)                    # If true then append the number only, the first value
        else:
            prime_numbers += ", " + str(number)             # Or else append a comma and num for succeeding values

print(f'Prime numbers: {prime_numbers}')                    # Print all the identified prime numbers