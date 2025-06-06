# PYBITES 5: Sum of Digits
# Task: Write a function to sum of Digits in a number.
# Example: input_numer = 1234 output = 10

input_number = 1234

def sum_digits(input_number):
    new_list = []
    for digit in str(input_number):
        new_list.append(int(digit))
    return sum(new_list)

print("Sum of digits:",sum_digits(input_number))
