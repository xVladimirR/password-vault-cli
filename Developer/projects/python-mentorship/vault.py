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

while True:
    print("\nPassword Vault")
    print("1. Add entry")
    print("2. View entries")
    print("3. Search by site")
    print("4. Exit")

    choise = input("Choose: ").strip()

    if choise == "1":
        add_entry()
    elif choise == "2":
        view_entries()
    elif choise ==  "3":
        serch_site()
    elif choise == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choise")
