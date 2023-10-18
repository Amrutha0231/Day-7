import hashlib

passwords = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_password():
    website = input("Enter the website or account name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    hashed_password = hash_password(password)
    
    passwords[website] = {
        "username": username,
        "password": password
    }
    print("Password added successfully!")

def retrieve_password():
    website = input("Enter the website or account name: ")
    if website in passwords:
        account = passwords[website]
        print(f"Username: {account['username']}")
        print(f"Password: {account['password']}")
    else:
        print("Website/account not found in the password manager.")

def update_password():
    website = input("Enter the website or account name: ")
    if website in passwords:
        password = input("Enter your new password: ")
        passwords[website]["password"] = password
        print("Password updated successfully!")
    else:
        print("Website/account not found in the password manager.")

while True:
    print("Choose an action:")
    print("1 - Add password")
    print("2 - Retrieve password")
    print("3 - Update password")
    print("4 - Exit")
    
    choice = input()
    
    if choice == '1':
        add_password()
    elif choice == '2':
        retrieve_password()
    elif choice == '3':
        update_password()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
