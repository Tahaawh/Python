temperatures = [] 

num_days = int(input("How many days of temperature data do you want to enter? ")) 

for i in range(num_days): 
    temp = float(input(f"Enter the temperature for day {i + 1}: ")) 
    temperatures.append(temp)  

count_above_30 = sum(1 for temp in temperatures if temp > 30) 

average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0

print(f"Number of days with temperatures above 30°C: {count_above_30}") 
print(f"{count_above_30} out of {num_days} days had temperatures above 30°C") 
print(f"Average temperature over {num_days} days: {average_temperature:.2f}°C")