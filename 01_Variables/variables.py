'''
=========================================================
CHAPTER 2 : VARIABLES AND OPERATIONS
=========================================================

What is a Variable?

A variable is a named location in memory that is used
to store data. The value stored in a variable can be
changed during the execution of a program.

Variables make programs easier to read, write,
and maintain because they allow us to reuse data
without writing the same value multiple times.

General Syntax:

variable_name = value

Examples:

name = "John"
age = 20
height = 1.75
is_student = True

In these examples:

- "name" stores a string.
- "age" stores an integer.
- "height" stores a floating-point number.
- "is_student" stores a Boolean value.

---------------------------------------------------------

Variable Naming Rules

When creating variables in Python, follow these rules:

1. A variable name must begin with a letter
   or an underscore (_).

2. A variable name cannot begin with a number.

3. A variable name can contain letters,
   numbers, and underscores.

4. Variable names are case-sensitive.

Example:

age = 20
Age = 25

These are considered two different variables.

5. Avoid using Python keywords as variable names.

Incorrect Examples:

2name = "John"
class = "Python"

---------------------------------------------------------

What are Operations?

Operations allow Python to manipulate data.
They are performed using operators.

The most common arithmetic operators are:

+   Addition

-   Subtraction

*   Multiplication

/   Division

//  Floor Division

%   Modulus (Remainder)

**  Exponentiation (Power)

Examples:

10 + 5      # Addition

10 - 5      # Subtraction

10 * 5      # Multiplication

10 / 5      # Division

10 // 3     # Floor Division

10 % 3      # Modulus

2 ** 4      # Exponentiation

---------------------------------------------------------

Order of Operations

Python follows the mathematical order of operations.

1. Parentheses ()
2. Exponentiation **
3. Multiplication *, Division /,
   Floor Division //, Modulus %
4. Addition + and Subtraction -

Example:

(2 + 3) * 4

Python first calculates:

2 + 3 = 5

Then:

5 * 4 = 20

---------------------------------------------------------

Why are Variables Important?

Variables allow programmers to:

• Store information.

• Reuse values.

• Perform calculations.

• Create dynamic programs.

• Make code easier to understand and maintain.

---------------------------------------------------------

Summary

✔ Variables store data.

✔ Variables can contain different data types.

✔ Operations manipulate data using operators.

✔ Python follows the order of operations
   when evaluating expressions.

The following exercises will help you practice
variables and arithmetic operations in Python.
'''
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
