username = input("Username: ")
password = input("Password: ")

found = False

with open("users.text", "r") as file:
    for line in file:
        saved_user, saved_pass = line.strip().split(",")

        if username == saved_user and password == saved_pass:
            print("Login successful")
            found = True
            break

if not found:
    print("Login failed")