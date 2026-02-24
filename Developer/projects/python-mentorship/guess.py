import random

secret = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("Correct!")

else:
    print(f"wrong! Number was {secret}")