def cmp_mm(a, b):
    """Compare two lists by their means and return sorted lists along with their means."""
    
    # Check if both lists are non-empty
    if not a or not b:
        raise ValueError("Both lists must contain at least one element.")

    # Calculate means
    m1 = sum(a) / len(a)
    m2 = sum(b) / len(b)

    # Sort lists
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    return m1, m2, a_sorted, b_sorted
