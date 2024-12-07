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

scores = list(student["scores"].values())

average = sum(scores) / len(scores)

student["average"] = average

print(student)