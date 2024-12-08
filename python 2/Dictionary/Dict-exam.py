studict={"name":"ali","family":"rad","marks":{"rizai":[13,14,11,17],"shimi":[19,12.5,11,14],"adabiat":[18,19,17,16.5]}}


M_times=[1, 2, 1, 4] 
all_sum = 0 
all_weight = 0 

print("average for each term:")
for term_index in range(4):
    term_sum = 0
    for subject, scores in studict["marks"].items():
        term_sum += scores[term_index]
    term_average = term_sum / len(studict["marks"])
    print(f"term {term_index + 1} average: {term_average}")

print("\n")

for keys, values in studict["marks"].items():
    total = 0
    for i in range(len(values)):
        total += values[i] * M_times[i] 
    average = total / 8

    print(f"{keys} overall average: {average}")
    all_sum += total
    all_weight += sum(M_times)

all_average = all_sum / all_weight
print(f"\noverall average for all subjects: {all_average}")