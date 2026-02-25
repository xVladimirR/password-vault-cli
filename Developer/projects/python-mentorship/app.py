def register():
    username = input("Create username: ")
    password = input("Create password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

        print("User registered")

def login():
    username = input("Username: ")
    password = input("Password: ")

    found = False

    with open("users.txt", "r") as file:
        for line in file:
            saved_user, saved_pass = line.strip().split(",")

            if username == saved_user and password == saved_pass:
                print("Login succsessful")
                found = True
                break
    if not found:
        print("Login failed")

while True:

    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()
    
    elif choice =="3":
        print("Goodbye")
        break
    
    else:
        print("Invalid choice")