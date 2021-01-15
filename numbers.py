# Python uses +, -, *, /, **
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(3**2)

# Python supports order of operation
print(2 + 3*4)
print((2 + 3) * 4)

# Floats are any number with a decimal
print(0.1 + 0.1)

# On occasion you'll run accross an arbitrary number of decimal places in your answer. We'll learn to deal with those later in Part 2 (projects)
print(0.2 + 0.1)

# Python defaults to floats wherever possible
print(4/2)

# If you mix integer and floats, you'll get a float
print(1 + 2.0)
print(3.0 ** 2)

# Python defaults to a float in any operation that uses a float, even if the output is a whole number.

# You can use underscores with large numbers to make it easier to read in code
# This is a newer feature in python 3.6
universeAge = 14_000_000_000
print(universeAge) # outputs 14000000000

# Multiple assignments
# You can assign values to more than one variable using a single line
x, y, z = 0, 0, 0

# Contants are a variable whose values stays the same throughout the life of a program (think let vs const in JS). These variables are denoted in all caps.
MAX_CONNECTIONS = 5000

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should simply be four lines with the number 8 appearing once
# on each line.

print(5+3)
print(10-2)
print(4*2)
print(2**3)

# 2-9. Favorite Number: Use a variable to represent your favorite number. Then,
# using that variable, create a message that reveals your favorite number. Print
# that message.

favouriteNumber = 1
message = f"{favouriteNumber} is my favourite number because it's the loneliest number of them all"
print(message)