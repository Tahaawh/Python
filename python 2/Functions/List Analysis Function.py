def analyze_lists(list1, list2):
    def median(lst):
        """Calculate the median of a list."""
        sorted_lst = sorted(lst)  # Create a sorted copy of the list
        n = len(sorted_lst)
        if n % 2 == 1:  # Odd length
            return sorted_lst[n // 2]
        else:  # Even length
            return (sorted_lst[n // 2] + sorted_lst[n // 2 - 1]) / 2

    def average(lst):
        """Calculate the average of a list."""
        if len(lst) == 0:
            return 0
        return sum(lst) / len(lst)

    avg1 = average(list1)
    avg2 = average(list2)
    med1 = median(list1)
    med2 = median(list2)

    compare_result1 = med1 >= avg1
    compare_result2 = med2 >= avg2

    return {
        'avg1': avg1,
        'avg2': avg2,
        'med1': med1,
        'med2': med2,
        'med1_ge_avg1': compare_result1,
        'med2_ge_avg2': compare_result2
    }

# Sample data
numbers1 = [12, 2, 3, 6, 55, 48, 5]
numbers2 = [20, 33, 66, 55, 45, 48]

# Analyzing the lists
results = analyze_lists(numbers1, numbers2)

# Printing the results
print("Average 1:", results['avg1'])
print("Average 2:", results['avg2'])
print("Median 1:", results['med1'])
print("Median 2:", results['med2'])
print("Median 1 >= Average 1:", results['med1_ge_avg1'])
print("Median 2 >= Average 2:", results['med2_ge_avg2'])
