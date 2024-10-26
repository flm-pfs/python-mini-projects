def remove_common_chars(name1, name2):
	# Find common characters between name1 and name2
	common_chars = set(name1) & set(name2)
	
	# Remove common characters from name1 and name2
	for char in common_chars:
		name1 = name1.replace(char, '', 1)
		name2 = name2.replace(char, '', 1)
	
	return name1, name2


def flames_game(name1, name2):
	# Convert names to lowercase and remove spaces
	name1 = name1.lower().replace(" ", "")
	name2 = name2.lower().replace(" ", "")

	# Remove common characters from names
	name1, name2 = remove_common_chars(name1, name2)

	# Calculate the count of remaining characters
	count = len(name1) + len(name2)

	# Define the flames options
	flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	# Perform the flames game
	while len(flames) > 1:
		index = (count % len(flames)) - 1
		if index >= 0:
			right = flames[index + 1:]
			left = flames[:index]
			flames = right + left
		else:
			flames = flames[:-1]

	return flames[0]


if __name__ == "__main__":
	# Get input names from the user
	name1 = input("Enter the first name: ")
	name2 = input("Enter the second name: ")
	
	# Calculate the relationship using flames game
	result = flames_game(name1, name2)
	
	# Print the result
	print(f"The relationship between {name1} and {name2} is: {result}")
