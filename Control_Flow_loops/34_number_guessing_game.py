'''Q34. Number Guessing Game

Set a secret number in your program.
Keep asking the user to guess until they get it right with hints.'''

secret_number = 25

guess = int(input("Guess the number: "))

while guess != secret_number:
    if guess > secret_number:
        print("Too High")
    else:
        print("Too Low")

    guess = int(input("Guess again: "))

print("Correct! 🎉")
