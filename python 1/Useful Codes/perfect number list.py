numbers = [12, 13, 11, 15, 16, 17, 9, 496, 19] 
perfect_numbers = []  
non_perfect_numbers = []  

for num in numbers: 
    sum_of_divisors = 0  
    
    for i in range(1, num): 
        if num % i == 0:  
            sum_of_divisors += i  

    if sum_of_divisors == num: 
        perfect_numbers.append(num)  
    else: 
        non_perfect_numbers.append(num)  

print("Perfect numbers:", perfect_numbers) 
print("Non-perfect numbers:", non_perfect_numbers)