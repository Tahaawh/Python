def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def separate_primes(numbers):
    """Separate prime numbers from non-prime numbers in a list."""
    primes = []
    non_primes = []
    
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)
    
    return primes, non_primes

# Example list of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate the numbers into primes and non-primes
primes, non_primes = separate_primes(numbers)

# Print the results
print("Prime numbers:", primes)
print("Non-prime numbers:", non_primes)
