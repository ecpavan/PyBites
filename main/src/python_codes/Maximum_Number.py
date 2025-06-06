# PYBITES 3: Find Maximum Number in a List
# Task: Use both the built-in max() function and a custom function to find the largest number in a list.
# Example: list_a = [1, 4, 6, 2, 44, 56] → Output: 56

input_list = [1, 4, 6, 2, 44, 56]

# Method 1: Using built-in max()
built_in_max = max(input_list)
print("Maximum number using built-in max():", built_in_max)

# Method 2: Custom function to find maximum
def find_max_number(input_list):
    max_number = input_list[0]
    for num in input_list[1:]:
        if num > max_number:
            max_number = num
    return max_number

print("Maximum number using custom function:", find_max_number(input_list))
