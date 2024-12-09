# Weighted average calculator for term and subject averages

data = {"name": "Ali", "surname": "Rad", "scores": {"math": [13, 14, 11, 17], "chem": [19, 12.5, 11, 14], "lit": [18, 19, 17, 16.5]}}
weights = [1, 2, 1, 4]

totalSum = 0
cumulativeSum = 0

print("Term Averages:")
for term in range(4):
    termTotal = 0
    for subject, marks in data["scores"].items():
        termTotal += marks[term]
    termAvg = f"{termTotal / len(data['scores']):.2f}"
    print(f"Term {term + 1}: {termAvg}")

print()

for subject, marks in data["scores"].items():
    weightedSum = 0
    for term in range(len(marks)):
        weightedSum += marks[term] * weights[term]
    subjectAvg = f"{weightedSum / sum(weights):.2f}"
    print(f"{subject.capitalize()} Avg: {subjectAvg}")
    totalSum += weightedSum
    cumulativeSum += sum(weights)

overallAvg = f"{totalSum / cumulativeSum:.2f}"
print(f"\nOverall Avg: {overallAvg}")