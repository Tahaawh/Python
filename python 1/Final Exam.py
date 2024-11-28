l=[12,17,18,6,9,19,28,23,18,11,16,15] 
list_3=[] 
list_cam=[] 
list_aval=[] 
not_cam=[] 
not_3=[] 
not_aval=[] 
l.sort() 
print(f"\n all number in main list:{l}\n") 
for num in l: 
    for i in range (2,num): 
        if num % i == 0: 
            not_aval.append(num) 
            break 
    else: 
        list_aval.append(num) 
list_aval.sort() 
print(f"prime number: {list_aval}") 
not_aval.sort() 
print(f"not prime number: {not_aval}\n") 
for num in l: 
    s=0 
    for i in range (1,num): 
        if num % i == 0: 
            s+=i 
    if s==num: 
        list_cam.append(num) 
    else: 
        not_cam.append(num) 
list_cam.sort() 
print(f"perfect number: {list_cam}") 
not_cam.sort() 
print(f"not perfect number: {not_cam}\n") 
for num in l: 
    for i in range (3,num): 
        if num % 3 == 0: 
            list_3.append(num) 
            break 
    else: 
        not_3.append(num) 
list_3.sort() 
print(f"number % 3: {list_3}") 
not_3.sort() 
print(f"not number % 3: {not_3}\n") 
