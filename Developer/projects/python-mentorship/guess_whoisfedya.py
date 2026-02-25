import random

hero = "Homeless"
secret = random.choice(["petuh", "ne petuh"])
attempts = 3

print("Welcome to the guessing game!")
print("You have 3 attempts.")

while attempts > 0:
    guess = input("Enter your name: ")

    if guess == hero:
        print(f"You win! You are {secret}")
    elif guess != hero:
        print(f"Try again Fistov!")
    else:
        print(f"You are stupid")

    attempts -= 1
    print(f"Attempts left {attempts}")

if attempts == 0:
    print(f"You brainless monkey. Number was {secret}")

print("Game over")