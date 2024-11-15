def cmp_mm(a, b):
    if not a or not b:
        raise ValueError("Both lists must contain at least one element.")

    m1 = sum(a) / len(a)
    m2 = sum(b) / len(b)

    return m1, m2, sorted(a), sorted(b)

# Example usage
a = [3, 1, 4, 1, 5]
b = [9, 2, 6, 5, 3]
result = cmp_mm(a, b)
print(result)