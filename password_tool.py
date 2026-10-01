"""
Password Hashing and Verification Tool

This program uses the bcrypt library to securely hash a password
and then verify that password against the generated hash. 
"""

import bcrypt
import getpass

def create_password():
    """Create a bcrypt hash and save it to a file."""
    while True:
        password = getpass.getpass("Enter a password to hash: ")
        match_password = getpass.getpass("Confirm the password: ")
        if password != match_password:
            print("Passwords do not match. Please try again.")
            continue
        password_strength_level = password_strength(password)
        print(f"Password strength: {password_strength_level}") 
        if password_strength_level == "Weak":
            print("Password is weak. Please choose a stronger password.")
            continue

        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        with open("hashed_password.txt", "wb") as f:
            f.write(hashed_password)

        print("New Password has been created.")
        break

def password_strength(password):
    """
    Check the strength of the password based on length and character variety.
    Returns a string indicating the strength level.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length < 8:
        return "Weak"
    elif length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

def verify_password():
    """
    This function prompts the user to enter a password and verifies it against the stored hashed password. 
    Additionally, it checks if the hashed password file exists and is not empty before proceeding with the verification.
    If the file does not exist or is empty, it informs the user to create a password first.
    """
    try:
        with open("hashed_password.txt", "rb") as f:
            hashed_password = f.read()

    except FileNotFoundError:
        print("No file found. Please create a password first.")
        return
    

    if not hashed_password:
        print("No hashed password found. Please create a password first.")
        return

    password_to_verify = getpass.getpass("Enter the password to verify: ")
    password_bytes = password_to_verify.encode('utf-8')

    if bcrypt.checkpw(password_bytes, hashed_password):
        print("Password matches the hash.")
    else:
        print("Password does not match the hash.")

while True:
    options = input("Enter 'New' to create a password or 'Verify' to verify a password or 'Exit' to quit: ").lower()

    if options == "new":
        create_password()
    elif options == "verify":
        verify_password()
    elif options == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please enter 'New' or 'Verify'.")
   