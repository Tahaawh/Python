def is_even(x):
    """Return True if x is even, otherwise False."""
    return x % 2 == 0

# Example input list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only even numbers
filtered_list = list(filter(is_even, num_list))

# Print the filtered list of even numbers
print(filtered_list)
