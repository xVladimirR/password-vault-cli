
VAULT_FILE = "vault.txt"


def read_entries():
    try:
        with open(VAULT_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def write_entries(lines):
    with open(VAULT_FILE, "w") as f:
        f.writelines(lines)


def add_entry(site, user, password):
    with open(VAULT_FILE, "a") as f:
        f.write(f"{site},{user},{password}\n")