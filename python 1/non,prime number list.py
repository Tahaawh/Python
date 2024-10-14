# List of numbers to be checked
numbers = [12, 13, 11, 15, 16, 17, 9, 7, 19] 
prime_numbers = []  # List to store prime numbers
non_prime_numbers = []  # List to store non-prime numbers

# Loop through each number in the numbers list
for num in numbers:
    # Assume the number is prime until proven otherwise
    if num < 2:  # Numbers less than 2 are not prime
        non_prime_numbers.append(num)
        continue
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:  # If num is divisible by any number other than 1 and itself
            non_prime_numbers.append(num)  # Add to non-prime numbers
            break
    else:
        prime_numbers.append(num)  # If no divisors were found, it's a prime number

# Print the lists of prime and non-prime numbers
print("Prime numbers:", prime_numbers)
print("Non-prime numbers:", non_prime_numbers)