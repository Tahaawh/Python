max_number = lambda x, y: x if x > y else y
power_five = lambda x: x ** 5
is_even = lambda x: x % 2 == 0
sign_func = lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero")
operation = lambda x, y: x ** 2 + y ** 2
compare_numbers = lambda a, b: f"greater {a} than {b}" if a > b else f"greater {b} than {a}"
prime_check = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))
SignFunc = lambda x, y: x if x > y else (y if x < y else "tie")
# Test Functions
print(max_number(7, 4))
print(power_five(2))
print(is_even(5))
print(sign_func(-3))
print(list(filter(lambda x: x % 2 == 0, [12, 14, 13, 16, 11, 18, 19, 7])))
print(operation(5, 8))
print(compare_numbers(65, -3))
print(prime_check(11))
print(SignFunc(5, 5))