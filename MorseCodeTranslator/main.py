class MorseCodeTranslator:
    def __init__(self):
        # Dictionary mapping English characters to Morse code
        self.morse_to_english = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
        }
        # Dictionary mapping Morse code to English characters
        self.english_to_morse = {value: key for key,
                                 value in self.morse_to_english.items()}

    def translate_to_morse(self, text):
        morse_code = []
        for char in text.upper():
            if char == ' ':
                morse_code.append(' ')
            elif char in self.morse_to_english:
                morse_code.append(self.morse_to_english[char])
        return ' '.join(morse_code)

    def translate_to_english(self, morse_code):
        english_text = []
        morse_words = morse_code.split('   ')
        for morse_word in morse_words:
            english_word = []
            morse_chars = morse_word.split()
            for morse_char in morse_chars:
                if morse_char in self.english_to_morse:
                    english_word.append(self.english_to_morse[morse_char])
            english_text.append(''.join(english_word))
        return ' '.join(english_text)

    def menu(self):
        while True:
            print("\nMorse Code Translator Menu:")
            print("1. Translate to Morse Code")
            print("2. Translate to English")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                text = input("Enter the text to translate to Morse Code: ")
                morse_code = self.translate_to_morse(text)
                print(f"Morse Code: {morse_code}")
            elif choice == '2':
                morse_code = input(
                    "Enter the Morse Code to translate to English: ")
                english_text = self.translate_to_english(morse_code)
                print(f"English Text: {english_text}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    translator = MorseCodeTranslator()
    translator.menu()
