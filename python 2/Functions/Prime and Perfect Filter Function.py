def separate(unit):
    def Nprime(NP):
        if NP < 2:
            return False
        for i in range(2, int(NP**0.5) + 1):
            if NP % i == 0:
                return False
        return True
    
    def Nperfect(NP):
        if NP < 2:
            return False
        div = [i for i in range(1, NP) if NP % i == 0]
        return sum(div) == NP
    
    # Filter the input list for prime and perfect numbers
    primes = list(filter(Nprime, unit))  # Simplified lambda function
    perfects = list(filter(Nperfect, unit))  # Simplified lambda function

    # Print results
    print("Prime Numbers:", primes)
    print("Perfect Numbers:", perfects)
    
    return primes, perfects

# Input list
input_list = [6, 28, 5, 12, 7, 496, 15, 8128, 13]
primes, perfects = separate(input_list)
