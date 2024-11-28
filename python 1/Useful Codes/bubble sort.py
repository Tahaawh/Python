def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:  
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

numbers = [12, 3, 11, 13, 14, 2, 1, 17, 5]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
