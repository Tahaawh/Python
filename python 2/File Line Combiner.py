def process_file(file_name):
    file = open(file_name + ".txt", 'r')
    file_lines = file.readlines()
    combined_lines = '*'.join(file_lines)
    file_lines.append(combined_lines)
    file.close()
    
    print("Done:", file_lines)

filename = input("Enter your file name: ")
process_file(filename)