import random

secret = random.randint(1, 10)
attempts = 3

print("Welcome to the guessing game!")
print("You have 3 attempts.")

while attempts > 0:
    guess = int(input("Enter your guess (1, 10): "))

    if guess == secret:
        print("You win!")
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

    attempts -= 1
    print(f"Attempts left {attempts}")

if attempts == 0:
    print(f"You lost. Number was {secret}")

print("Game over")