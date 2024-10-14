# List manipulations
lst1 = [3, 4, 5, 6, 7]
lst2 = [1, 2, 8, 9]

# Append each item in lst2 to lst1
for i in lst2:
    lst1.append(i)

# Extend lst1 with all elements from lst2
lst1.extend(lst2)

# Inserting 3 at index 1 in a new list
lst = [1, 2, 4, 5, 6]
lst.insert(1, 3)  # lst becomes [1, 3, 2, 4, 5, 6]

# Modifying a new list
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst.remove(4)  # Removes first occurrence of 4
del lst[7]     # Deletes the element at index 7 (now 8)
if 3 in lst:
    lst.remove(3)  # Removes 3 if it is in lst

# Name manipulation
lstname = ["ali", "sara", "reza", "mohammad"]
lstname2 = ["elham", "zahra", "niusha"]
lstname2.insert(1, lstname.pop(1))  # Moves "sara" from lstname to lstname2
print(lstname)  # ['ali', 'reza', 'mohammad']
print(lstname2)  # ['elham', 'sara', 'zahra', 'niusha']

# More list operations
lst = [3, 2, 5, 10, 1]
# Note: Indexing out of range here, so we will comment it out
# x = lst.index(5, 3, 6)  # This line would raise an error since there’s no index 6
lst.clear()  # Clears the list
# The following code block will not execute because lst is empty now
# for i in range(len(lst) - 1, -1, -1):  
#     x = lst.pop(i)  
#     lst.append(x)  
lst.sort(reverse=True)  # Sorting an empty list remains empty
lst.reverse()           # Reversing an empty list remains empty
print(lst.count(5))    # Counts occurrences of 5 in an empty list, should return 0

# Store line example
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")  # Inserts "Vikor" at index 2
print(store_line)  # ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']

# Soup examples
soups = ['minestrone', 'lentil', 'pho', 'laksa']
print(soups[-1])      # 'laksa'
print(soups[-3:])     # ['lentil', 'pho', 'laksa']
print(soups[:-2])     # ['minestrone', 'lentil']

# CS topics manipulation
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()  # Removes the last element
print(cs_topics)                   # Updated list
print(removed_element)             # 'Clowns 101'

# Class name hobbies manipulation
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
class_name_hobbies[0][1] = "Meditation"  # Changes "Breakdancing" to "Meditation"
print(class_name_hobbies)

# Heights manipulation
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
noelles_height = heights[0][1]  # Gets Noelle's height
print(noelles_height)             # Prints 61

# Tools manipulation
tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3]  # Slices tools list to get ['hammer', 'lever']
tools_slice[0] = 'nail'    # Changes 'hammer' to 'nail' in the slice
print(tools_slice)         # Prints ['nail', 'lever']