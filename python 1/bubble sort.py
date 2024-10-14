def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n - 1 - i):
            # Traverse the array from 0 to n-i-1
            if numbers[j] > numbers[j + 1]:  # Compare adjacent elements
                # Swap if the element found is greater than the next element
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# List of numbers to be sorted
numbers = [12, 3, 11, 13, 14, 2, 1, 17, 5]
sorted_numbers = bubble_sort(numbers)

# Print the sorted list
print(sorted_numbers)
