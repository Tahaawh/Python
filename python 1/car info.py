def find_car(car_models, prices, availability, car_name):
    car_name = car_name.strip()  # Remove leading/trailing whitespace
    found = False 

    for i in range(len(car_models)): 
        if car_name.lower() == car_models[i].lower():  # Case-insensitive comparison
            print(f"Car model: {car_models[i]}") 
            print(f"Price: ${prices[i]}") 
            print(f"Status: {availability[i]}") 
            found = True 
            break  # Exit the loop once the car is found

    if not found: 
        print(f"{car_name} not available")

# Lists of car details
car_models = ["Tesla Model S", "Ford Mustang", "BMW X5", "Audi A4", "Chevrolet Camaro"] 
prices = [79999, 55000, 62000, 45000, 42000] 
availability = ["Coming Soon…", "Not Available", "Available", "Available", "Not Available"] 

# Input from user
car_name = input("Enter a car model: ")
find_car(car_models, prices, availability, car_name)
