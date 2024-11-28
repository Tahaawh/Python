def files(fileName):
    file = open(fileName + ".txt", 'r')
    str2 = file.readlines()
    str3 = '*'.join(str2)
    str2.append(str3)
    file.close()
    
    print("done:", str2)

filename = input("Enter your file name: ")
files(filename)