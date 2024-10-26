import random


class Chatbot:
    def __init__(self):
        # List of greetings
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]

        # List of goodbyes
        self.goodbyes = ["Goodbye!", "See you later!",
                         "Bye!", "Have a great day!"]

        # List of questions
        self.questions = ["How can I help you today?", "What can I do for you?",
                          "Is there anything specific you need help with?"]

        # List of unknown responses
        self.unknown_responses = ["I'm not sure I understand.",
                                  "Could you please rephrase that?", "I didn't catch that."]

        # Knowledge base with predefined responses
        self.knowledge_base = {
            "weather": "I'm sorry, I can't provide real-time data.",
            "time": "I'm sorry, I can't provide real-time data.",
            "joke": "Why don't scientists trust atoms? Because they make up everything!"
        }

    def respond(self, user_input):
        user_input = user_input.lower()

        # Check if user input contains a greeting
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.greetings)

        # Check if user input contains a goodbye
        elif "bye" in user_input or "goodbye" in user_input:
            return random.choice(self.goodbyes)

        # Check if user input contains a request for help
        elif "help" in user_input:
            return random.choice(self.questions)

        else:
            # Check if user input matches any key in the knowledge base
            for key in self.knowledge_base:
                if key in user_input:
                    return self.knowledge_base[key]

            # If no match found, return a random unknown response
            return random.choice(self.unknown_responses)

    def chat(self):
        print("Chatbot: " + random.choice(self.greetings))
        while True:
            user_input = input("You: ")

            # Check if user wants to end the conversation
            if user_input.lower() in ["bye", "goodbye"]:
                print("Chatbot: " + random.choice(self.goodbyes))
                break

            # Get response from the chatbot
            response = self.respond(user_input)
            print("Chatbot: " + response)


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
