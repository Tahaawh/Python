numbers = [12, 13, 11, 15, 16, 17, 9, 7, 19] 
prime_numbers = []  
non_prime_numbers = []  

for num in numbers:
    if num < 2:  
        non_prime_numbers.append(num)
        continue
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:  
            non_prime_numbers.append(num)  
            break
    else:
        prime_numbers.append(num)
         
print("Prime numbers:", prime_numbers)
print("Non-prime numbers:", non_prime_numbers)