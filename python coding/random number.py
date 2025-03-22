import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
guess = None

print("I'm thinking of a number between 1 and 100. Can you guess it?")
print("You have 10 attempts. Good luck!\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!\n")
        elif guess > secret_number:
            print("Too High!\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s).")
            break

        # Show a hint after 5 incorrect attempts
        if attempts == 5:
            # Find a factor of the secret number (other than 1 and the number itself)
            for i in range(2, secret_number):
                if secret_number % i == 0:
                    print(f"💡 Hint: The number is divisible by {i}.\n")
                    break

    except ValueError:
        print("Please enter a valid number.\n")

# If max attempts reached and not guessed
if guess != secret_number:
    print(f"❌   You've used all {max_attempts} attempts. The number was {secret_number}. Better luck next time!")
