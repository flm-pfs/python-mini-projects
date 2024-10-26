import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "Happiness can exist only in acceptance. - George Orwell"
]


def get_random_quote():
    """
    Returns a random quote from the list of quotes.
    """
    return random.choice(quotes)


def main():
    """
    Main function that runs the Random Quote Generator.
    """
    print("Welcome to the Random Quote Generator!")
    while True:
        enter = input(
            "Press Enter to get a random quote or type 'exit' to quit: ")
        if (enter == "exit"):
            break
        print("\n" + get_random_quote() + "\n")


if __name__ == "__main__":
    main()
