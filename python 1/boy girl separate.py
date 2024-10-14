# List of names categorized into boys and girls
names = [
    ["reza", "ali", "nima", "hasan"], 
    ["sara", "elham", "elaheh", "maryam", "zahra"]
] 

# Lists to hold boys' and girls' names
boys_names = [] 
girls_names = [] 

# Iterate through the names list
for index in range(len(names)): 
    if index == 0:  # First sub-list contains boys' names
        boys_names.extend(names[index]) 
    else:  # Any other sub-lists contain girls' names
        girls_names.extend(names[index]) 

# Print the results
print("Boys' Names:", boys_names) 
print("Girls' Names:", girls_names) 
