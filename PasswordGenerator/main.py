import random
import string


def generate_password(length=12):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt the user to enter the length of the password
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            # Generate a password of the specified length
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")


if __name__ == "__main__":
    main()
