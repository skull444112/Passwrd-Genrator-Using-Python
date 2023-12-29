import random, string

CHARS = string.ascii_letters + string.digits + string.punctuation

def generate_password(length: int) -> str:
    password = random.choices(CHARS, k=length)
    random.shuffle(password)
    return "".join(password)


def generate_passwords(num: int, file: str) -> None:
    if not 1 <= num <= 100:
        raise ValueError("Invalid number")
    passwords = set()
    while len(passwords) < num:
        length = random.randint(6, 16)
        password = generate_password(length)
        passwords.add(password)
    with open(f"{file}.txt", "a") as f:
        for password in passwords:
            f.write(f"\nPassword: {password}\n---------")
            print(f"Password: {password}\n---------")
    print(f"Passwords generated and written to {file}")

passwords = int(input("How many Passwords do you want?: "))
file = input("Enter the file name: ")
try:
    generate_passwords(passwords, file)
except ValueError as e:
    print(e)
input("press enter to continue..")
