import bcrypt
import time
import re

# Simulated secure user database (with pre-hashed password)
users = {
    "admin": bcrypt.hashpw("Admin@123".encode(), bcrypt.gensalt()),
    "user1": bcrypt.hashpw("Password!456".encode(), bcrypt.gensalt())
}

# Simple input validation (username and password format)
def is_valid_username(username):
    return re.match(r"^[a-zA-Z0-9_]{3,20}$", username)

def is_valid_password(password):
    return len(password) >= 6

# Login function with brute-force protection
def login():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        # Input validation
        if not is_valid_username(username):
            print("❌ Invalid username format.")
            continue

        if not is_valid_password(password):
            print("❌ Password too short.")
            continue

        # Authentication
        if username in users and bcrypt.checkpw(password.encode(), users[username]):
            print("✅ Login successful!")
            return True
        else:
            print("❌ Login failed.")
            attempts += 1
            print(f"⏳ Attempts left: {max_attempts - attempts}")

        time.sleep(1)  # Prevent brute force with delay

    print("🚫 Too many failed attempts. Try again later.")
    return False

# Start the login process
if __name__ == "__main__":
    print("🔐 Welcome to the Secure Login System")
    login()