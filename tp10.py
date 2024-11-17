def backup_file(source_file, backup_file):
    source = open(source_file, 'r')
    data = source.read()
    source.close()

    backup = open(backup_file, 'w')
    backup.write(data)
    backup.close()

    print("Backup completed successfully!")

source = "file1.txt"
backup = "backup_file1.txt"
backup_file(source, backup)


riazi=20 shimi=17
hendeseh=18.5
arabi-15
farsi=19
varzesh=20
english=18


def calculate_average(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    
    scores = [float(line.strip()) for line in lines if line.strip()]
    
    if len(scores) > 0:
        average = sum(scores) / len(scores)
        print(round(average, 1))
    else:
        print("No scores found.")

file_path = input("Enter file path: ")
calculate_average(file_path)

f1 = open("new.txt", 'r+')
s2 = f1.read()
f1.seek(10, 0)
lines = s2.split("\n")

for i in range(len(lines)):
    if i % 2 == 0:
        f1.write("*\n")
    else:
        f1.write(lines[i] + "\n")

f1.close()

