def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return odd_numbers, even_numbers

input_list = [1, 2, 3, 6, 5, 4, 8, 9]
odds, evens = separate_odd_even(input_list)

print("Even Numbers:", evens)
print("Odd Numbers:", odds)
