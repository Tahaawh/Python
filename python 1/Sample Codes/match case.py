role = input("Enter your role (Admin/Accountant/Employee/Manager): ")

match role:
    case "Admin":
        password = input("Enter your password: ")
        if password == "adminPass":
            print("Welcome, Admin!")
        else:
            print("Password or role is wrong. Please run the program again.")
    case "Accountant":
        password = input("Enter your password: ")
        if password == "accountantPass":
            print("Welcome, Accountant!")
        else:
            print("Password or role is wrong. Please run the program again.")
    case "Employee":
        password = input("Enter your password: ")
        if password == "employeePass":
            print("Welcome, Employee!")
        else:
            print("Password or role is wrong. Please run the program again.")
    case "Manager":
        password = input("Enter your password: ")
        if password == "managerPass":
            print("Welcome, Manager!")
        else:
            print("Password or role is wrong. Please run the program again.")
    case _:
        print("Invalid role. Please run the program again.")