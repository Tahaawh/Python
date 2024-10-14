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
lst = [12, 15, 16, 18, 17, 99, 13, 11]

# Initialize lists for prime and non-prime numbers
prime_list = [num for num in lst if is_prime(num)]
non_prime_list = [num for num in lst if not is_prime(num)]

# Print the filtered lists of prime and non-prime numbers
print(f"Prime numbers: {prime_list}")
print(f"Not prime numbers: {non_prime_list}")
