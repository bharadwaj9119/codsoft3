import secrets
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    characters = ""
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set must be selected.")
        return None

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
