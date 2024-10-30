import random
import string

def generate_password(length=12):
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4.")
    else:
        # Generate and print the password
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for length.")