password = input("Enter password: ")

if len(password) < 6:
    print("Password too short")
elif password == "123456":
    print("Password too weak")
elif password == "admin":
    print("Password too obvious")
else:
    print("Password accepted")