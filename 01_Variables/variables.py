'''
=========================================================
EXERCISES - CHAPTER 2: VARIABLES AND OPERATIONS IN PYTHON
=========================================================

Exercise 1: Friedman Numbers

Friedman numbers are numbers that can be expressed
using all of their digits in a mathematical expression.

Example:
347 = 4 + 7**3

Instructions:

Determine whether the following expressions correspond
to Friedman numbers.

To do this:

1. Write each expression in Python.
2. Execute it.
3. Check whether the result is equal to the number
   formed by the digits used.
'''

print("========== Exercise 1 ==========\n")

print("Question 1: 7 + 3**6")

# I think Python will first calculate 3**6,
# then add 7 to the result.

print("Result:", 7 + 3**6)

print("\n---------------------------------\n")

print("Question 2: (3 + 4)**3")

# I think Python will first calculate
# the addition of 3 and 4,
# then raise the result to the power of 3.

print("Result:", (3 + 4)**3)

print("\n---------------------------------\n")

print("Question 3: 3**6 - 5")

# Python first calculates 3**6,
# then subtracts 5.

print("Result:", 3**6 - 5)

print("\n---------------------------------\n")

print("Question 4: (1 + 2**8) * 5")

# Python first calculates 2**8.
# Then it adds 1.
# Finally, it multiplies the result by 5.

print("Result:", (1 + 2**8) * 5)

print("\n---------------------------------\n")

print("Question 5: (2 + 1**8)**7")

# Python first calculates 1**8.
# Then it adds 2.
# Finally, it raises the result
# to the power of 7.

print("Result:", (2 + 1**8)**7)

print("\n\n")

'''
=========================================================
Exercise 2: Predict the Result of Operations
=========================================================

Instructions:

Try to predict the result of each instruction
before running it in Python.

Then compare your prediction
with the actual result.
'''

print("========== Exercise 2 ==========\n")

print("Question 1: (1 + 2) ** 3")

# Python first performs the addition.
# Then it raises the result
# to the power of 3.

print("Result:", (1 + 2) ** 3)

print("\n---------------------------------\n")

print('Question 2: "Da" * 4')

# Python repeats the string
# "Da" four times.

print("Result:", "Da" * 4)

print("\n---------------------------------\n")

print('Question 3: "Da" + 3')

# I think an error will occur.
# In Python, you cannot add
# a string (str)
# and an integer (int).

# print("Da" + 3)

print("Expected Result: TypeError")

print("\n---------------------------------\n")

print('Question 4: ("Pa" + "La") * 2')

# Python first concatenates
# the two strings.
# Then it repeats the result twice.

print("Result:", ("Pa" + "La") * 2)

print("\n---------------------------------\n")

print('Question 5: ("Da" * 4) / 2')

# I think an error will occur.
# Division is not allowed
# on a string.

# print(("Da" * 4) / 2)

print("Expected Result: TypeError")

print("\n---------------------------------\n")

print("Question 6: 5 / 2")

# Standard division
# always returns a floating-point number.

print("Result:", 5 / 2)

print("\n---------------------------------\n")

print("Question 7: 5 // 2")

# Floor division returns
# only the integer part.

print("Result:", 5 // 2)

print("\n---------------------------------\n")

print("Question 8: 5 % 2")

# The modulo operator returns
# the remainder of the division.

print("Result:", 5 % 2)

print("\n\n")

'''
=========================================================
Exercise 3: Operations and Type Conversions
=========================================================

Instructions:

Predict the result of each instruction
before running it.

Then verify your answer
by executing the code.
'''

print("========== Exercise 3 ==========\n")

print('Question 1: str(4) * int("3")')

# int("3") becomes 3.
# str(4) becomes "4".
# Python repeats the string "4"
# three times.

print("Result:", str(4) * int("3"))

print("\n---------------------------------\n")

print('Question 2: int("3") + float("3.2")')

# int("3") becomes 3.
# float("3.2") becomes 3.2.
# Python then performs the addition.

print("Result:", int("3") + float("3.2"))

print("\n---------------------------------\n")

print('Question 3: str(3) * float("3.2")')

# I think an error will occur.
# A string cannot be multiplied
# by a floating-point number (float).

# print(str(3) * float("3.2"))

print("Expected Result: TypeError")

print("\n---------------------------------\n")

print("Question 4: str(3 / 4) * 2")

# Python first calculates 3 / 4.
# Then it converts the result
# into a string.
# Finally, it repeats
# the string twice.

print("Result:", str(3 / 4) * 2)
