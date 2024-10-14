# Lambda function to find the maximum of two numbers
max_number = lambda x, y: x if x > y else y
print(max_number(7, 4))

# Lambda function to raise a number to the power of five
power_five = lambda x: x ** 5
print(power_five(2))

# Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(5))

# Lambda function to determine the sign of a number
sign_func = lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero")
print(sign_func(-3))

# List of numbers to filter even numbers
num_list = [12, 14, 13, 16, 11, 18, 19, 7]
print(list(filter(lambda x: x % 2 == 0, num_list)))

# Lambda function to perform an operation on two numbers (squares)
operation = lambda x, y: x ** 2 + y ** 2
print(operation(5, 8))

# Lambda function to compare two numbers
compare_numbers = lambda a, b: f"greater {a} than {b}" if a > b else f"greater {b} than {a}"
print(compare_numbers(65, -3))

# Lambda function to check if a number is prime
prime_check = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))
print(prime_check(11))

# Lambda function to determine the relation between two numbers
SignFunc = lambda x, y: x if x > y else (y if x < y else "tie")
print(SignFunc(5, 5))