student = {
    "name": "Nima",
    "surname": "Jafari",
    "id": "5678",
    "grades": [15.5, 18, 17.25, 19, 16.5]
}

grades = student["grades"]
average = sum(grades) / len(grades)

student["average"] = average

print(student)