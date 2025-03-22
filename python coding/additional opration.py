def calculator():
    while True:
        try:
            # Take input from user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform operations
            print("\n--- Results ---")
            print(f"Addition: {num1 + num2}")
            print(f"Subtraction: {num1 - num2}")
            print(f"Multiplication: {num1 * num2}")
            print(f"Division: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")
            print(f"Modulus: {num1 % num2 if num2 != 0 else 'Cannot calculate modulus with zero'}")
            print(f"Exponentiation: {num1 ** num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Ask if the user wants to continue
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Calculator exited.")
            break
        print()  # Just for a clean line between sessions

# Run the calculator
calculator()
