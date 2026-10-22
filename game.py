
import random

secret_number = random.randint(1, 100)
attempts = 0

print("=" * 35)
print("     NUMBER GUESSING GAME")
print("=" * 35)
print("I have selected a number from 1 to 100.")
print("Try to guess it!")

while True:
    guess_text = input("\nEnter your guess: ")

    if not guess_text.isdigit():
        print("Please enter a valid whole number.")
        continue

    guess = int(guess_text)

    if guess < 1 or guess > 100:
        print("Choose a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try a bigger number.")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print(f"Correct! You won in {attempts} attempts!")
        break

print("Thanks for playing!")
