def valid_num(phone):
    if phone.startswith("09") and len(phone) == 11 and phone.isdigit():
        return "Valid phone number."
    else:
        return "Invalid phone number."
while True:
    phone = input("Enter phone number: ")
    result = valid_num(phone)
    print(result)
    if result=="Valid phone number.":
        break