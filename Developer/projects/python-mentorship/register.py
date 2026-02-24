username = input("Create username: ")
password = input("Create password: ")

with open("users.text", "a") as file:
    file.write(username + "," + password + "\n")

print("User registered successfully")