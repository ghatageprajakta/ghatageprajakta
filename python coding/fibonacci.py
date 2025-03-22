def fibonacci_loop(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Fibonacci using recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Get user input
try:
    n_terms = int(input("Enter the number of Fibonacci terms to generate: "))

    if n_terms <= 0:
        print("Please enter a positive number.")
    else:
        # Using loop
        print("\nFibonacci sequence using loop:")
        print(fibonacci_loop(n_terms))

        # Using recursion
        print("\nFibonacci sequence using recursion:")
        for i in range(n_terms):
            print(fibonacci_recursive(i), end=" ")
        print()

except ValueError:
    print("Invalid input! Please enter a valid integer.")
