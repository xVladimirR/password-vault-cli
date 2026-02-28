
from vault.manager import list_entries, create_entry

def main():
    while True:
        print("\nPassword Vault")
        print("1. Add Entry")
        print("2. View entries")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choise")

if __name__ == "__main__":
    main()