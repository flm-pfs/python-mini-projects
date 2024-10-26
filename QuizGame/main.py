import random

# List of questions with their options and answers
questions = [
	{
		"question": "What is the capital of France?",
		"options": ["Berlin", "Madrid", "Paris", "Rome"],
		"answer": "Paris"
	},
	{
		"question": "Which planet is known as the Red Planet?",
		"options": ["Earth", "Mars", "Jupiter", "Venus"],
		"answer": "Mars"
	},
	{
		"question": "What is the largest mammal?",
		"options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
		"answer": "Blue Whale"
	}
]

def ask_question(question_data):
	"""
	Asks a single question to the user and checks if the answer is correct.

	Args:
		question_data (dict): Dictionary containing the question, options, and answer.

	Returns:
		bool: True if the user's answer is correct, False otherwise.
	"""
	print(question_data["question"])
	for i, option in enumerate(question_data["options"]):
		print(f"{i + 1}. {option}")
	user_answer = input("Enter the number of your answer: ")
	try:
		user_answer = int(user_answer)
		if 1 <= user_answer <= len(question_data["options"]):
			return question_data["options"][user_answer - 1] == question_data["answer"]
		else:
			print("Invalid option number. Please try again.")
			return ask_question(question_data)
	except ValueError:
		print("Please enter a valid number.")
		return ask_question(question_data)

def quiz_game():
	"""
	Main function to run the quiz game.

	Prints the welcome message, shuffles the questions, asks each question,
	and calculates the final score.
	"""
	print("Welcome to the Quiz Game!")
	random.shuffle(questions)
	score = 0
	for question in questions:
		if ask_question(question):
			print("Correct!\n")
			score += 1
		else:
			print(f"Wrong! The correct answer is {question['answer']}\n")
	print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
	quiz_game()