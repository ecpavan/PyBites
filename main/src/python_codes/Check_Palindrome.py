# PYBITES 2: Check Palindrome
# Task: Given a string and check if it's a palindrome.

input_string = input("Enter a word: ")
reversed_string = input_string[::-1]

if input_string == reversed_string:
    print(f"The word '{input_string}' is a palindrome.")
else:
    print(f"The word '{input_string}' is not a palindrome.")
