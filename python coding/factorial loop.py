def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else: 
        print(f"Factorial of {number} using loop: {factorial_loop(number)}")
        print(f"Factorial of {number} using recursion: {factorial_recursive(number)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
