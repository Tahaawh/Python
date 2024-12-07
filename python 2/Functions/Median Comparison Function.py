def calculate_median(data):
    """Calculate the median of a sorted list."""
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return data[mid]
    else:
        return (data[mid] + data[mid - 1]) / 2

def compare_medians(list1, list2):
    """Compare two lists by their medians and return the list with the higher median."""
    
    # Sort the lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    # Calculate medians
    median1 = calculate_median(sorted_list1)
    median2 = calculate_median(sorted_list2)

    # Return the list with the higher median
    return sorted_list1 if median1 > median2 else sorted_list2

# Example usage
list1 = [3, 8, 2, 9, 6]
list2 = [10, 11, 20, 12, 16]
result = compare_medians(list1, list2)
print(result)
