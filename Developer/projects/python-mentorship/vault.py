VAULT_FILE = "vault.txt"

def add_entry():
    site = input("Site: (exemple: gmail): ").strip()
    user = input("Username/email ").strip()
    pw = input("Password: ").strip()

    with open(VAULT_FILE, "a") as f:
        f.write(f"{site},{user},{pw}\n")

        print("Saved ✅")

def view_entries():
    try:
        with open(VAULT_FILE, "r") as f:
            lines = f.readlines()
            
        if not lines:
            print("Vault is empty.")
            return
        print("\n--- VAULT ---")
        for i, line in enumerate(lines, start=1):
            site, user, password = line.strip().split(",", 2)
            masked = password[:2] + "***"
            print(f"{i}. {site} | {user} |{masked}")
        
    except FileNotFoundError:
        print("Vault is empty (no file yet).")

def serch_site():
    query = input("Search site: ").strip().lower()
    found_any = False

    try:
        with open(VAULT_FILE, "r") as f:
            for line in f:
                site, user, pw = line.strip().split(",", 2)
                if query in site.lower():
                    print(f"{site} | {user} | {pw}")
                    found_any = True
    except FileNotFoundError:
        pass
    if not found_any:
        print("No matches.")

def delete_entry():
    try:
        with open(VAULT_FILE, "r") as f:
            lines = f.readlines()

        if not lines:
            print("Vault empty.")
            return
        
        for i, line in enumerate(lines, start=1):
            site, user, pw = line.strip().split(",", 2)
            print(f"{i}. {site} | {user}")

        choise = int(input("Enter entry number to delete: "))

        if 1 <= choise <= len(lines):
            lines.pop(choise - 1)

            with open(VAULT_FILE, "w") as f:
                f.writelines(lines)

            print("Deleted.")
        else:
            print("Invalid number.")

    except FileNotFoundError:
        print("Vault empty.")

def edit_entry():
    try:
        with open(VAULT_FILE, "r") as f:
            lines = f.readlines()

        if not lines:
            print("Vault empty.")
            return
        
        for i, line in enumerate(lines, start=1):
            site, user, pw = line.strip().split(",", 2)
            print(f"{i}. {site} | {user}")
        
        choise = int(input("Enter entry number to edit: "))

        if 1 <= choise <= len(lines):
            
            new_site = input("New site: ")
            new_user = input("New username: ")
            new_pw = input("New password: ")

            lines[choise - 1] = f"{new_site},{new_user},{new_pw}\n"

            with open(VAULT_FILE,"w") as f:
                f.writelines(lines)

            print("Updated.")
        
        else:
            print("Invalid number.")

    except FileNotFoundError:
        print("Vault empty.")

while True:
    print("\nPassword Vault")
    print("1. Add entry")
    print("2. View entries")
    print("3. Search by site")
    print("4. Edit entry")
    print("5. Delete entry")
    print("6. Exit")

    choise = input("Choose: ").strip()

    if choise == "1":
        add_entry()
    elif choise == "2":
        view_entries()
    elif choise ==  "3":
        serch_site()
    elif choise == "4":
        edit_entry()
    elif choise =="5":
        delete_entry()
    elif choise == "6":
        print("Goodbye")
        break
    else:
        print("Invalid choise")
