# PYBITES 4: Count Vowels in a String
# Task: Write a function to count the number of vowels in a given string.
# Example: input_string = "hello_world"

vowels = ['a','e','i','o','u']  # defines standard lowercase vowels

input_string = "hello_world"   # Example input

def vowels_count(input_string):  
    vowel_count = 0
    for letter in input_string:       
        if letter.lower() in vowels:   #Checks letter with Case-insensitive comparison 
            vowel_count = vowel_count + 1  # Adds to count
    return vowel_count

print(vowels_count(input_string))  
