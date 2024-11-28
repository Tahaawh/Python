i = 1
for count_2000 in range(11): 
    for count_5000 in range(5): 
        for count_10000 in range(3):
            total = count_2000 * 2000 + count_5000 * 5000 + count_10000 * 10000
            if total == 20000:
                components = []
                if count_2000 != 0:
                    components.append(f"{count_2000} x 2000")
                if count_5000 != 0:
                    components.append(f"{count_5000} x 5000")
                if count_10000 != 0:
                    components.append(f"{count_10000} x 10000")
                
                answer = " + ".join(components)
                print(f"Answer number {i}:   {answer} = Can make 20,000 Tomans\n")
                i += 1
