import bcrypt

password = input("Enter a password to hash: ")

password_bytes = password.encode('utf-8')

hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("Thank, you will be asked again to verify the password.")  

verify_password = input("Enter the password again to verify: ")
verify_password_bytes = verify_password.encode('utf-8') 

if bcrypt.checkpw(verify_password_bytes, hashed_password):
    print("Password matches the hash.")
else:
    print("Password does not match the hash.")