# 1. append(x): Adds an element to the end of the list
lst = [1, 2]
lst.append(3)  # [1, 2, 3]

# 2. extend(iterable): Adds all elements from an iterable to the end of the list
lst = [1, 2]
lst.extend([3, 4])  # [1, 2, 3, 4]

# 3. insert(index, x): Inserts an element at a specific index
lst = [1, 3]
lst.insert(1, 2)  # [1, 2, 3]

# 4. remove(x): Removes the first occurrence of an element
lst = [1, 2, 3]
lst.remove(2)  # [1, 3]

# 5. del lst[index]: Deletes the element at a specific index
lst = [1, 2, 3]
del lst[1]  # [1, 3]

# 6. pop([index]): Removes and returns the element at the specified index
lst = [1, 2, 3]
removed_element = lst.pop()  # [1, 2], removed_element = 3

# 7. clear(): Removes all elements from the list
lst = [1, 2, 3]
lst.clear()  # []

# 8. sort(reverse=False): Sorts the list in ascending order (or descending if reverse=True)
lst = [3, 1, 2]
lst.sort()  # [1, 2, 3]
lst.sort(reverse=True)  # [3, 2, 1]

# 9. reverse(): Reverses the order of the list
lst = [1, 2, 3]
lst.reverse()  # [3, 2, 1]

# 10. count(x): Counts the occurrences of an element in the list
lst = [1, 2, 2]
count_of_2 = lst.count(2)  # 2

# 11. Slicing: Creates a sublist using index range
lst = [1, 2, 3, 4]
sub_list = lst[1:3]  # [2, 3]

# 12. Nested Indexing: Modify values in nested lists
nested_lst = [["Jenny", "Breakdancing"]]
nested_lst[0][1] = "Meditation"  # [["Jenny", "Meditation"]]

# 13. index(x, start, end): Finds the index of the first occurrence of an element within a specified range
lst = [1, 2, 3]
index_of_2 = lst.index(2)  # 1