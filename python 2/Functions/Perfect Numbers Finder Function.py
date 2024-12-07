def is_perfect(numbers):
    """Return a list of perfect numbers from the given list of numbers."""
    perfect_numbers = []
    
    for num in numbers:
        if num < 1:  # Ignore non-positive integers
            continue

        divisor_sum = sum(i for i in range(1, num) if num % i == 0)
        
        if divisor_sum == num:
            perfect_numbers.append(num)
    
    return perfect_numbers

# Example usage
a = [10, 4, 6, 31, 12, 8, 96, 28, 496]
perfect_nums = is_perfect(a)
print(perfect_nums)
