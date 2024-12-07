def sum_lists(list1, list2):
    result_list = []
    for i in range(len(list1)):
        result_list.append(list1[i] + list2[i])
    return result_list

# Testing the function with two lists
output = sum_lists([1, 2, 3], [4, 5, 6])
print(output)  # Output: [5, 7, 9]
