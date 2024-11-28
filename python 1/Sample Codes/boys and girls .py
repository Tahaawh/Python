names = [["reza", "ali", "nima", "hasan"], ["sara", "elham", "elaheh", "maryam", "zahra"]] 

boys_names = [] 
girls_names = [] 

for index in range(len(names)): 
    if index == 0:  
        boys_names.extend(names[index]) 
    else:  
        girls_names.extend(names[index]) 

print("Boys' Names:", boys_names) 
print("Girls' Names:", girls_names) 
