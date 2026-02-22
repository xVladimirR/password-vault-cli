# 1 age next year
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")

# 2 sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum = {a + b}")

# 3 uppercase
word = input("Enter a word: ")
print(word.upper())

# 4 characters count
sentence = ("Enter a sentence: ")
print(f"Characters {len(sentence)}")

# 5 even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")