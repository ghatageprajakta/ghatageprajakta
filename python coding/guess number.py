import random

# Step 1: Generate a random number between 1 and 50
secret_number = random.randint(1, 50)
print(f"(Debug) The secret number is: {secret_number}")  # <-- Add this line for testing
attempts = 0
guess = None

print("I'm thinking of a number between 1 and 50. Can you guess it?")

# Step 2–4: User guesses until correct
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
    except ValueError:
        print("Please enter a valid number.")



