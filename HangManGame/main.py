import random


def choose_word():
    # List of words to choose from
    words = ["apple", "banana", "cherry", "date",
             "elderberry", "fig", "grape", "honeydew"]
    return random.choice(words)


def display_word(word, guessed_letters):
    # Display the word with guessed letters filled in
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            if set(word) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            if attempts == 0:
                print("\nYou lost! The word was:", word)
                break

    if attempts == 0:
        print("\nYou lost! The word was:", word)


if __name__ == "__main__":
    hangman()
