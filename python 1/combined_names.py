name_parts = [["taha", "reza", "mohammad"], ["ahmadi", "sorant", "akhvan"]] 

# Using list comprehension to combine names
combined_names = [f"{first} {last}" for first, last in zip(name_parts[0], name_parts[1])]

# Print the combined names
print(combined_names)
