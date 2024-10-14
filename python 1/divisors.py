numbers = [12, 13, 6, 28, 474, 11, 15, 16, 17, 9, 7, 19]
divisors_list = []

for num in numbers:
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    divisors_list.append(divisors)

print(divisors_list)
