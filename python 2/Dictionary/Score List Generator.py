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

score_list = list(student["scores"].values())

print(score_list)