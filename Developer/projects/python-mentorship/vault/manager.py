
from vault.storage import read_entries, write_entries, add_entry


def list_entries():
    lines = read_entries()
    if not lines:
        print("Vault is empty.")
        return

    print("\n--- VAULT ---")
    for i, line in enumerate(lines, start=1):
        site, user, password = line.strip().split(",", 2)
        masked = password[:2] + "***"
        print(f"{i}. {site} | {user} | {masked}")


def create_entry():
    site = input("Site: ").strip()
    user = input("Username: ").strip()
    password = input("Password: ").strip()

    add_entry(site, user, password)
    print("Saved ✅")