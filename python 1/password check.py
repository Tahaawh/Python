# Main password
mainpass = 1234 

# Allow up to 3 attempts for entering the password
for i in range(1, 4): 
    password = int(input("Enter password: "))  # Prompt user for password
    
    if password == mainpass:  # Check if the entered password is correct
        print("Welcome")
        break  # Exit the loop if the password is correct
    elif i != 3:  # If this is not the last attempt
        print("Try Again!!!")  # Prompt to try again
    else:  # If this was the last attempt
        print("Expired!!!")  # Inform user that attempts have expired