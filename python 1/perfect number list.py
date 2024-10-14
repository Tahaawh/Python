# List of numbers to be checked
numbers = [12, 13, 11, 15, 16, 17, 9, 7, 19] 
perfect_numbers = []  # List to store perfect numbers
non_perfect_numbers = []  # List to store non-perfect numbers

# Loop through each number in the numbers list
for num in numbers: 
    sum_of_divisors = 0  # Initialize the sum of divisors for the current number
    
    # Loop through potential divisors from 1 to num - 1
    for i in range(1, num): 
        if num % i == 0:  # Check if i is a divisor of num
            sum_of_divisors += i  # Add i to the sum of divisors

    # Check if the sum of divisors equals the number itself
    if sum_of_divisors == num: 
        perfect_numbers.append(num)  # It's a perfect number
    else: 
        non_perfect_numbers.append(num)  # It's not a perfect number

# Print the lists of perfect and non-perfect numbers
print("Perfect numbers:", perfect_numbers) 
print("Non-perfect numbers:", non_perfect_numbers)