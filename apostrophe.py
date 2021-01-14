message = "One of Python's strengths is its diverse community."
print(message)

# Syntax error due to single quotes
# You can't use single quotes within a single quote. Python is unable to determine where the string should end.
# As a result you get a syntax error.
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# 2.3 Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name = "billy"
print(f"Hello, {name.title()}, would you like to learn some Python today?")

# 2.4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

newName = "billy bob"
print(newName.lower())
print(newName.upper())
print(newName.title())

# 2.5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”

print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')

# 2.6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.

famousPerson = "Albert Einstein"
message = f'{famousPerson} once said, "A person who never made a mistake never tried anything new"'
print(message)

# 2.7. Stripping Names: Use a variable to represent a person’s name, and include
# some whitespace characters at the beginning and end of the name. Make sure
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

person = " john \n\tdoe "
print(person)
print(person.lstrip())
print(person.rstrip())
print(person.strip())
