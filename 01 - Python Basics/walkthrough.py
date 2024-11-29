# Ignore this for now
import random


# Quick Python examples to get familiar with the syntax

print('Hello world!')
# Outputs: Hello world!

# This python file will walk through some of the basic concepts of Python that
# will be needed for programming robots

#
# Comments
#

# print('This is commented out!)
print('This line will print')
# Outputs: This line will print

# Only Python code can be in a Python file, anything that isn't Python code
# needs to be commented, which you can do with "#". Python will ignore anything
# after a "#" character, this can be code you don't want to run or comments
# explaining what code does

#
# Types
#

# Strings - strings are characters
'this is a string'

# Integers - integers are whole numbers
5
-103
2024
100000005

# Floats - floats are decimal numbers
1.6
-4.558
-26000.2

# Booleans - "True" or "False"
True
False

#
# Variables
#
# Variables are used to store values within the code and can be assigned using
# a single "="

variable_x = 'this is a string variable'

# This is also a variable, but an integer
y = 5

# This is a variable, but a float
z = 1.25

# Variables can also store calculated values

y = y + z
print(y)
# Outputs: 6.25

# 6.25 + 6.25 = 12.5
y = y + y
print(y)
# Outputs: 12.5


print('\nConditionals and Logic Section:\n')
#
# Conditional Statements and Logic
#
# Conditions and Logic are written to make different "decisions" or branches in
# your code


# Boolean variables (True or False) can be calculated by "expressions"
true_value = 10 > 5
print('true_value: ' + str(true_value))
# Outputs: True

# Because 10 is greater than 5

false_value = 'string1' == 'string2'
print('false_value: ' + str(false_value))
# Outputs: False

# Because 'string1' is not the same as 'string2'

# If-Else Statement
#
# If-Else statements are used often in code to create different "branches" or
# paths through code

# Generate a random variable between 1 and 100
random_variable = random.randint(1,100)

print('Randomly generated variable: ' + str(random_variable)) # Convert int to string to combine

if random_variable > 50:
  # If variable is larger than 50, print this message
  print("That's a big number")
else:
  # Otherwise, print this message
  print("That's a small number, try again!")

#
# You can add additional conditions to if-else statements in Python using "elif"
#

if random_variable >= 90:
  # if random_variable is greater than or equal to 90
  print('You got an A')
elif random_variable >= 80:
  print('You got an B')
elif random_variable >= 70:
  print('You got an C')
elif random_variable >= 65:
  print('You got an D')
else:
  print('You failed')

# If statements are evaluated in order, so in the case above we can use the
# order of the statements to our advantage, to know what grade range we are in
# for each case.
#
# if the first if statement is False, we know that the grade is below a 90, so
# the second statement essentially checks if the grade is between 80-89



print('\nLoops Section:\n')
#
# Loops
#
# Loops are essential in Robotics and programming in general. Loops allow code
# to be run multiple times based on the condition you provide. There are 2 main
# types of loops "For" loops and "While" Loops. Each have specific cases where
# they make more sense
#


#
# While loop
#
# A while loop will run until the condition provided is False. to create an
# infinite loop, you could write a while loop such as 'while True:'
#
print('While Loop:')
counter = 0

while counter < 5:
  # Print out the current counter value
  print(counter)
  # Add one to the counter during this loop
  counter = counter + 1
print('Final counter value: ' + str(counter))

# Outputs: 0
#          1
#          2
#          3
#          4
#          Final counter value: 5

# This loop prints out 0-4, because the loop runs until the counter is not less
# than 5, and 5 is not less than 5


#
# For loop
#
# A for loop runs for a pre-determined number of times.
print('\nFor Loops:')

# This loop will print out each letter in the word 'word'
for letter_variable in 'word':
  # on each loop, the next character in the string is assigned to the variable
  # 'letter_variable'
  print(letter_variable)

# Outputs: w
#          o
#          r
#          d

print()

# range() is a function commonly used with for loops to specify the number of
# times to run. in this case range(0, 3) evaluates to 0, 1, 2 so the loop runs 3
# times
for i in range(0,3):
  print(i)

# Outputs: 0
#          1
#          2


print('\nFunctions Section:\n')
#
# Functions
#
# Functions are essential for programming. A function is a chunk of code that
# can be called repeatedly and makes code reuseable
#


# Below is a function that prints out a message
def write_message():
  print('Secret message')

# This is another function that takes 'parameters' or variables as inputs. This
# is used often so a function can be used in multiple ways
def write_messages(recipient, times):
  for i in range(0,times):
    print('Hello ' + recipient + ', from Computer')

# This function takes a parameter 'number' and returns a value. In this case, it
# returns a Boolean, True if the number provided is bigger than 50, False if the
# number is 50 or less
def is_number_big(number):
  if number > 50:
    return True
  else:
    return False

# Functions are called by their name followed by parenthesis
write_message()
# Outputs: Secret Message

write_messages('Programmer', 2)
# Outputs: Hello Programmer, from Computer
#          Hello Programmer, from Computer

write_messages('Coder', 1)
# Outputs: Hello Coder, from Computer

print()

variable_1 = is_number_big(99)
print('variable_1: ' + str(variable_1))
# Outputs: True

print()

print(is_number_big(-100))
# Outputs: False