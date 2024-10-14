# Prompt user for a number
num = int(input("Enter a number: ")) 

# Check for primality
if num <= 1:
    print("Not Prime")  # Numbers less than or equal to 1 are not prime
else:
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:  # Check if num is divisible by i
            print("Not Prime") 
            break  # Exit the loop if a divisor is found
    else: 
        print("Prime Number")  # No divisors found, num is prime