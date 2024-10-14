# List of names grouped into two sublists
names = [["reza", "ali", "nima", "hasan"], ["sara", "elham", "elaheh", "maryam", "zahra"]]
names_with_m = []  # List to store names containing 'm'

# Loop through each group of names
for group in names:
    # Loop through each name in the current group
    for name in group:
        # Check if 'm' is in the name
        if "m" in name:
            names_with_m.append(name)  # Add name to the list if it contains 'm'

# Print the list of names containing 'm'
print(names_with_m)