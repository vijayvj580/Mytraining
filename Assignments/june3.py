#1

def sum_of_odd_digits(number):
    odd_sum = 0
    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            odd_sum += digit
        number //= 10
    return odd_sum

def sum_of_even_digits(number):
    even_sum = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_sum += digit
        number //= 10
    return even_sum

def difference_between_sums(number):
    odd_sum = sum_of_odd_digits(number)
    even_sum = sum_of_even_digits(number)
    return odd_sum - even_sum

# Test the functions
number = int(input("Enter a number: "))

# Calculate and print the difference between the sums of odd and even digits
result = difference_between_sums(number)
print("Difference between sums of odd and even digits:", result)



#2

import re
def find_python_occurrences(text):
    pattern = r'\bPython\b'
    occurrences = re.findall(pattern, text)
    return occurrences

# Test the function
text = "Python is a great programming language. Python is widely used in various fields."
python_occurrences = find_python_occurrences(text)
print("Occurrences of 'Python':", python_occurrences)


#3

import math

def calculate_square_root():
    try:
        number = float(input("Enter a non-negative number: "))
        if number < 0:
            raise ValueError("Negative number entered. Please enter a non-negative number.")
        square_root = math.sqrt(number)
    except ValueError as ve:
        print("Error:", ve)
    except NameError as ne:
        print("Error:", ne)
    else:
        print("Square root:", square_root)
    finally:
        print("Program execution completed.")

calculate_square_root()