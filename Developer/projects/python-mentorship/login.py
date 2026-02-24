username = "admin"
password = "python123"
attempts = 3

while attempts > 0:

    input_user = input("Username: ")
    input_pass = input("Password: ")

    if input_user == username and input_pass == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Access denied. Attempts left: {attempts}")

if attempts == 0:
    print("Account locked")