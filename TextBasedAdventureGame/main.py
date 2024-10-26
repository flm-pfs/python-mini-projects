import time


def print_slow(text):
    # Function to print text slowly
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def start_game():
    # Function to start the game
    print_slow("Welcome to the Text-Based Adventure Game!")
    print_slow("You are standing in front of a dark cave.")
    print_slow("Do you want to enter the cave? (yes/no)")

    choice = input().lower()
    if choice == 'yes':
        enter_cave()
    elif choice == 'no':
        print_slow("You decide not to enter the cave and go back home.")
    else:
        print_slow("Invalid choice. Please enter 'yes' or 'no'.")
        start_game()


def enter_cave():
    # Function to handle entering the cave
    print_slow("You enter the dark cave.")
    print_slow("You see two paths ahead. One to the left and one to the right.")
    print_slow("Which path do you choose? (left/right)")

    choice = input().lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print_slow("Invalid choice. Please enter 'left' or 'right'.")
        enter_cave()


def left_path():
    # Function to handle taking the left path
    print_slow("You take the left path.")
    print_slow("You find a treasure chest!")
    print_slow("Do you want to open it? (yes/no)")

    choice = input().lower()
    if choice == 'yes':
        print_slow("You open the chest and find a pile of gold!")
        print_slow("Congratulations! You win the game!")
    elif choice == 'no':
        print_slow("You decide not to open the chest and continue exploring.")
        print_slow("You find nothing else and exit the cave.")
    else:
        print_slow("Invalid choice. Please enter 'yes' or 'no'.")
        left_path()


def right_path():
    # Function to handle taking the right path
    print_slow("You take the right path.")
    print_slow("You encounter a sleeping dragon!")
    print_slow(
        "Do you want to sneak past the dragon or turn back? (sneak/turn back)")

    choice = input().lower()
    if choice == 'sneak':
        print_slow("You try to sneak past the dragon.")
        print_slow("The dragon wakes up and eats you!")
        print_slow("Game over!")
    elif choice == 'turn back':
        print_slow("You decide to turn back and take the left path.")
        left_path()
    else:
        print_slow("Invalid choice. Please enter 'sneak' or 'turn back'.")
        right_path()


if __name__ == "__main__":
    start_game()
