# PYBITES 6: Check if two strings are anagrams
# Task: Write a function to check if two strings are anagrams.
# Examples: word1 = "kaka"  word2 = "akka"
word1 = input("enter the sting 1: ")
word2 = input("enter the sting 2: ")

if sorted(word1) == sorted(word2):
    print(f"{word1} and {word2} are anagram")
else:
    print(f"{word1} and {word2} are not anagram")
