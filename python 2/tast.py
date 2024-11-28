def get_info():
    def get_valid_input(prompt, validation_func):
        while True:
            value = input(prompt)
            if validation_func(value):
                return value
            else:
                print("Invalid input, please try again.")
    
    def is_name_valid(name):
        return name.isalpha()

    def is_family_valid(family):
        return family.isalpha()

    def is_average_valid(average):
        try:
            avg = float(average)
            return 0 <= avg <= 20  # average must be between 0 and 20
        except ValueError:
            return False

    def is_idnum_valid(idnum):
        return idnum.isdigit() and len(idnum) == 10  # ID number must be 10 digits

    name = get_valid_input("Enter your name: ", is_name_valid)
    family = get_valid_input("Enter your family name: ", is_family_valid)
    average = get_valid_input("Enter your average score: ", is_average_valid)
    idnum = get_valid_input("Enter your ID number: ", is_idnum_valid)

    return {
        "name": name,
        "family": family,
        "average": average,
        "idnum": idnum
    }

# Call the function
info = get_info()
print("The entered information was successfully recorded:")
print(f"Name: {info['name']}, Family: {info['family']}, Average: {info['average']}, ID: {info['idnum']}")