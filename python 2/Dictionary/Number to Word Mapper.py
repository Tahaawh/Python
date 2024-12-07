numbers = [1, 2, 3, 4, 5]
words = ["one", "two", "three", "four", "five"]

number_dict = {}

for index, num in enumerate(numbers):
    number_dict[num] = words[index]

print(number_dict)