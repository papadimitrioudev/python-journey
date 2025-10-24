# A simple guessing game that demonstrates while True, break and continue.

import random

# Generate a secret number between 1 and 10
secret = random.randint(1, 10)

# Keep looping until the user guesses correctly
while True:
    # Ask the user for a guess
    guess = int(input("Guess the number (1-10): "))

    # If the guess is out of range, skip the rest of the loop
    if guess < 1 or guess > 10:
        print("Out of range, try again.")
        continue

    # Provide feedback
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        # Correct guess: end the game
        print(f"You found it! The number was {secret}.")
        break