import random


def get_user_choice():
    # Prompt the user to choose Rock, Paper, or Scissors
    while True:
        user_choice = input(
            "Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def get_computer_choice():
    # Generate a random choice for the computer
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the user's choice and the computer's choice
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    # Main function to play the game
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()
