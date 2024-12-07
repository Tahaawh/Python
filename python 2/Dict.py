# در ادامه، تمامی کدها با خروجی‌های مورد انتظار به‌صورت کامنت در انتها آورده شده‌اند:

# کد 1: به‌روزرسانی یک دیکشنری

student_scores = {'Ali': 85, 'Reza': 92}
new_scores = {'Reza': 95, 'Sara': 88}

student_scores.update(new_scores)
print(student_scores)

# خروجی:
# {'Ali': 85, 'Reza': 95, 'Sara': 88}

# کد 2: مدیریت دیکشنری با عملیات مختلف

info = {"name": "Hassan", "surname": "Rahimi", "id": "1234567890", "average": 16.8}

# اضافه کردن آدرس
info["address"] = "Isfahan"

# تغییر مقدار میانگین
info["average"] = 17.9

# حذف کلید "id"
del info["id"]

# چاپ دیکشنری به‌روز شده
print(info)

# خروجی:
# {'name': 'Hassan', 'surname': 'Rahimi', 'average': 17.9, 'address': 'Isfahan'}

# کد 3: کار با کلیدها و مقادیر دیکشنری

person = {"name": "Mina", "surname": "Zarei", "id": "456789123", "average": 18.2}

# بررسی وجود کلید "id" در دیکشنری
print("id" in person)

# تعداد کلیدها در دیکشنری
print(len(person))

# لیست کلیدها
keys_list = list(person.keys())
print(keys_list)

# لیست مقادیر
values_list = list(person.values())
print(values_list)

# خروجی:
# True
# 4
# ['name', 'surname', 'id', 'average']
# ['Mina', 'Zarei', '456789123', 18.2]

# کد 4: چاپ کلید-مقدارهای دیکشنری

person = {"name": "Fatemeh", "surname": "Kiani", "id": "9988776655", "average": 19.1}

# چاپ کلید-مقدارها با حلقه
for key, value in person.items():
    print(key, value)

# چاپ آیتم‌های دیکشنری
print(person.items())

# خروجی:
# name Fatemeh
# surname Kiani
# id 9988776655
# average 19.1
# dict_items([('name', 'Fatemeh'), ('surname', 'Kiani'), ('id', '9988776655'), ('average', 19.1)])

# کد 5: ایجاد دیکشنری از دو لیست

numbers = [1, 2, 3, 4, 5]
words = ["one", "two", "three", "four", "five"]

# دیکشنری خالی
number_dict = {}

# پر کردن دیکشنری با حلقه
for index, num in enumerate(numbers):
    number_dict[num] = words[index]

print(number_dict)

# خروجی:
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# کد 6: حذف کلید با استفاده از pop

number_dict = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty"}
removed_value = number_dict.pop(40)  # حذف مقدار کلید 40
print(number_dict)

# خروجی:
# {10: 'ten', 20: 'twenty', 30: 'thirty'}

# کد 7: حذف آخرین آیتم با popitem

data = {1: "a", 2: "b", 3: "c", 4: "d"}

# حذف آخرین آیتم
last_item = data.popitem()

print(last_item)  # چاپ آیتم حذف شده
print(data)  # چاپ دیکشنری پس از حذف

# خروجی:
# (4, 'd')
# {1: 'a', 2: 'b', 3: 'c'}

# کد 8: مرتب‌سازی دیکشنری بر اساس کلیدها

unsorted_data = {5: "e", 2: "b", 1: "a", 3: "c"}
sorted_data = dict(sorted(unsorted_data.items()))  # مرتب‌سازی بر اساس کلیدها
print(sorted_data)

# خروجی:
# {1: 'a', 2: 'b', 3: 'c', 5: 'e'}

# کد 9: میانگین نمرات یک دانش‌آموز از لیست نمرات

student = {
    "name": "Nima",
    "surname": "Jafari",
    "id": "5678",
    "grades": [15.5, 18, 17.25, 19, 16.5]
}

# محاسبه میانگین
grades = student["grades"]
average = sum(grades) / len(grades)

# افزودن میانگین به دیکشنری
student["average"] = average

print(student)

# خروجی:
# {'name': 'Nima', 'surname': 'Jafari', 'id': '5678', 'grades': [15.5, 18, 17.25, 19, 16.5], 'average': 17.45}

# کد 10: استخراج لیستی از مقادیر دیکشنری تو در تو

student = {
    "name": "Ahmad",
    "surname": "Karimi",
    "id": "1234",
    "scores": {
        "math": 18.5,
        "physics": 17.75,
        "chemistry": 19,
        "sports": 20
    }
}

# استخراج مقادیر دیکشنری داخلی
score_list = list(student["scores"].values())

print(score_list)

# خروجی:
# [18.5, 17.75, 19, 20]

# کد 11: محاسبه میانگین نمرات از دیکشنری تو در تو

student = {
    "name": "Maryam",
    "surname": "Bahrami",
    "id": "8765",
    "scores": {
        "math": 19,
        "history": 18.75,
        "english": 17.5,
        "sports": 20
    }
}

# استخراج مقادیر دیکشنری تو در تو
scores = list(student["scores"].values())

# محاسبه میانگین
average = sum(scores) / len(scores)

# اضافه کردن میانگین به دیکشنری اصلی
student["average"] = average

print(student)

# خروجی:
# {'name': 'Maryam', 'surname': 'Bahrami', 'id': '8765', 'scores': {'math': 19, 'history': 18.75, 'english': 17.5, 'sports': 20}, 'average': 18.8125}