names = [["reza", "ali", "nima", "hasan"], ["sara", "elham", "elaheh", "maryam", "zahra"]]
names_with_m = [] 

for group in names:
    for name in group:
        if "m" in name:
            names_with_m.append(name) 
print(names_with_m)