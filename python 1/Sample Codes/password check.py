mainpass = 1234 

for i in range(1, 4): 
    password = int(input("Enter password: "))  
    
    if password == mainpass:  
        print("Welcome")
        break 
    elif i != 3: 
        print("Try Again!!!")  
    else:  
        print("Expired!!!")  