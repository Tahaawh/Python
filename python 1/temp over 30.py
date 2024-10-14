# Initialize an empty list to store temperatures
temperatures = [] 

# Prompt user for the number of days of temperature data
num_days = int(input("How many days of temperature data do you want to enter? ")) 

# Loop to collect temperature data for the specified number of days
for i in range(num_days): 
    temp = float(input(f"Enter the temperature for day {i + 1}: ")) 
    temperatures.append(temp)  # Append the entered temperature to the list

# Count the number of days with temperatures above 30°C
count_above_30 = sum(1 for temp in temperatures if temp > 30) 

# Calculate the average temperature
average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0

# Print the results
print(f"Number of days with temperatures above 30°C: {count_above_30}") 
print(f"{count_above_30} out of {num_days} days had temperatures above 30°C") 
print(f"Average temperature over {num_days} days: {average_temperature:.2f}°C")