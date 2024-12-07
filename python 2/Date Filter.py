text = "Example: In this text, dates like 2023/11/01 and 23/05/15 and 2024/04/05 are included."
words = text.split()
dates = []

for word in words:
    if word.count("/") == 2 and (len(word) == 10 or len(word) == 8):
        parts = word.split("/")
        if all(part.isdigit() for part in parts):
            year, month, day = parts
            if (len(year) in [2, 4]) and len(month) == 2 and len(day) == 2:
                dates.append(word)

for date in dates:
    print(f"{date} : its_date.")