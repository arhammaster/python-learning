string = "Hello, World! Welcome to Python programming."

# Original
print(string)

# Convert to uppercase
uppercase_string = string.upper()
print(uppercase_string)

# Convert to lowercase
lowercase_string = string.lower()
print(lowercase_string)

# Convert to title case
title_case_string = string.title()
print(title_case_string)

# Print first character
print(string[0])

# Print fifth character
print(string[4])

# Print last character
print(string[-1])

# Print first five character
print(string[0 : 5])

# Print character from 8 to 13 characters
print(string[7 : 13])

# Trim operations
string_with_spaces = "   Hello World    " 
print(string_with_spaces.strip())
print(string_with_spaces.rstrip())
print(string_with_spaces.lstrip())

# String check - is Hello is prt of String 
print("Hello" in string)
print("planet" not in string)

# Multi line string
multi_line_string = """
---------------------------
Hello world
good morning
---------------------------
""" 
print(multi_line_string)

# Join strings

first_name = "Jack"
last_name = "Smith"

full_name1 = first_name + ' ' + last_name
print(full_name1)

full_name2 = f'{first_name} {last_name}'
print(full_name2)