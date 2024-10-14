def calculate_median(lst):
    """Calculate the median of a sorted list."""
    lst.sort()  # Sort the list to calculate the median
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

def calculate_mean(lst):
    """Calculate the mean of a list."""
    return sum(lst) / len(lst) if lst else 0

def cmp_mm(list1, list2):
    """Compare two lists and return the greatest median and mean."""
    median1 = calculate_median(list1)
    median2 = calculate_median(list2)
    
    mean1 = calculate_mean(list1)
    mean2 = calculate_mean(list2)
    
    greatest_median = max(median1, median2)
    greatest_mean = max(mean1, mean2)

    return greatest_median, greatest_mean

# Sample lists
l1 = [11, 13, 17, 61, 19, 23]
l2 = [2, 34, 56, 18, 10, 72]

# Calculate the greatest median and mean
lm, lm_mean = cmp_mm(l1, l2)

# Print results
print(f"Greatest median: {lm}")
print(f"Greatest mean: {lm_mean}")
