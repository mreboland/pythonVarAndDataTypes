firstName = "ada"
lastName = "lovelace"
# the 'f' refers to an f-string in python. The 'f' stands for format and it tells python to replace or format the name of any variable with it's value. Similar function to tilde in JS ``
fullName = f"{firstName} {lastName}"
print(fullName)

# Using f-strings to compose a complete message
print(f"Hello, {fullName.title()}")

# Using f-strings to compose a message assigned to a variable
# Useful for simplifying the print call
message = f"Hello, {fullName.title()}!"
print(message)

# Python 3.5 or earlier uses format()
# Each variable is referred to by a set of braces; the braces will be filled by the values listed in parentheses in the order provided.
fullName = "{} {}".format(firstName, lastName)
print(fullName)


# Whitespace, tabs, and newlines

print("Python")
# tab
print("\tPython")
# Newline
print("Languages:\nPython\nJS\nReact")
# Tabs and Newline
print("Languages:\n\tPython\n\tJS\n\tReact")

# Removing whitespace. Terminal doesn't show the whitespace however run the code in python interpreter and i'll show the whitespace
favouriteLanguage = "python "
print(favouriteLanguage)
# Calling the below will print python without the whitespace however it only temp modified the variable. If you were to print the variable again after the strip it would have the whitespace again
# rstrip() removes whitespace from the right
print(favouriteLanguage.rstrip())
# In order to save the whitespace edit, you need to save it to a variable
favouriteLanguage = favouriteLanguage.rstrip()
print(favouriteLanguage)

favouriteLanguage = " python "
# Left whitespace
favouriteLanguage.lstrip()
# Both sides stripped
favouriteLanguage.strip()