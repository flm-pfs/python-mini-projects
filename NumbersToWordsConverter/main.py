def number_to_words(num):
    if num == 0:
        return "zero"

    # Define word mappings for numbers
    ones = ["", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def helper(n):
        if n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return ones[n // 100] + " hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        return ""

    result = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + (" " + thousands[i] if i != 0 else "") + (
                " " + result if result != "" else "")
        num //= 1000
        i += 1

    return result.strip()


# Take input from the user
try:
    number = int(input("Enter a number: "))
    print(number_to_words(number))
except ValueError:
    print("Invalid input. Please enter a valid number.")
