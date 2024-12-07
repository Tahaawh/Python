import math

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# List of numbers to check for primality
lst = [12, 17, 15, 11, 19, 21, 23, 27]

# Use list comprehension to create a list of prime numbers
prime_list = [num for num in lst if is_prime(num)]

# Print the filtered list of prime numbers
print(f"Prime numbers: {prime_list}")
