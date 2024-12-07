def even_odd(n):
    """Return 'even' if the number is even, otherwise return 'odd'."""
    return "even" if n % 2 == 0 else "odd"

def main():
    try:
        x = int(input("Enter a number: "))
        print(f"The number {x} is {even_odd(x)}.")
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
