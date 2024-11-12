# Program 1: Phone Number Extraction from Text
text = '''Iran endured invasions by the Macedonians, 09122501580 Arabs, Turks, and Mongols. Despite these invasions:
Iran remained a monarchy until 09121941560 the 1979 Iranian Revolution, when it officially 09121929161 became'''

words = text.split()
phone_numbers = []

for word in words:
    if word.isdigit() and word.startswith("091") and len(word) == 11:
        phone_numbers.append(word)

print(f"{phone_numbers} : Valid phone numbers.")


# Program 2: Email Validation Function
def validate_email(email_str):
    is_valid = False
    if '@' in email_str and '.' in email_str:
        at_index = email_str.index('@')
        dot_index = email_str.rindex('.')
        if at_index > 0 and dot_index >= 3 and dot_index > at_index:
            if len(email_str[dot_index + 1:]) >= 2:
                is_valid = True
    return is_valid

email_to_check = "hello@gmail.com"
print(validate_email(email_to_check))

emails_list = "taha@gmail.com ali@icloud.com hosein.yahoo@com"
emails = emails_list.split()
print(emails)

valid_emails = []
for email in emails:
    if validate_email(email):
        valid_emails.append(email)

print(valid_emails)


# Program 3: Writing to a File
file1 = open("file1.txt", 'a')
file1.write("Meisam \nakhavan\tTeacher")
file1.close()


# Program 4: File Writing from List of Names

def create_file(filename, content):
    file = open(filename + ".txt", 'w')
    file.write(content)
    file.close()
    print("Done")

filename_input = input("Enter file name:")
content_input = input("Enter your content:")
create_file(filename_input, content_input)


# Program 5: Reading from a File
file_contents = []
file1 = open("taha12.txt", 'r')
file_content = file1.read()
file_contents.append(file_content)
file1.close()
print(file_contents)


# Program 6: Reading Until a Specific Line (e.g., Break on "*")
file3 = open("file1.txt", 'r')
while True:
    if file3.readline() == "*":
        break
    line = file3.readline()
    print(line)
file3.close()


# Program 7: File Processing and Appending Text
def process_file(file_name):
    file = open(file_name + ".txt", 'r')
    file_lines = file.readlines()
    new_line = "*".join(file_lines)
    file_lines.append(new_line)
    file.close()

    print("done:", file_lines)

file_name_input = input("Enter your file name:")
process_file(file_name_input)


# Program 8: File Processing with Split Operation
def process_file(file_name):
    file = open(file_name + "-txt", 'r')
    file_content = file.read()
    word_list = file_content.split()
    file.close()
    return word_list

file_name_input = input("Enter your file name: ")
words_from_file = process_file(file_name_input)
print(words_from_file)


# Program 13: File Processing and Writing Again
file_contents = []
file1 = open("taha12.txt", 'r')
file_content = file1.read()
split_content = file_content.split()
file1.close()
print(split_content)


# Program 14: Generate and Append to New File
def append_to_new_file(filename, content_to_append):
    new_file = open(filename + "txt", 'a')
    new_file.write(content_to_append)
    new_file.close()
    print("New file done.")

file_name_input = input("Name for your new file:")
content_to_append_input = input("Enter your content to append:")
append_to_new_file(file_name_input, content_to_append_input)


# Program 15: Read Content of File and Print
file3 = open("file1.txt", 'r')
file_content = file3.read()
print(file_content)
file3.close()


# Program 16: Reading Each Line of File Until Empty
file3 = open("file1.txt", 'r')
while True:
    line = file3.readline()
    if line == "":
        break
    print(line)
file3.close()