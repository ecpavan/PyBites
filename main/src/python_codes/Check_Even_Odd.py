# PYBITES 7: Check the number even or odd
# Task: Write a function to Check the number even or odd.
# Examples: number 12,13
num = int(input("enter the number : "))

def even_or_odd(number):
    if num%2 == 0:
        print(f"Entered number {num} is Even")
    else:
        print(f"Entered number {num} is Odd")

even_or_odd(num)    
