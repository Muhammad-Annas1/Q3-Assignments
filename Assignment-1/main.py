print ("Hello World!")

def greet(name):
    return f"Hello,{name}!"
print () #print a new line
print(greet("Annas"))

# Data Types

# String
name="Annas"
print() #print a new line
print(name)

# Integer
age=26
print() #print a new line
print(age)

# Float
width=10.5
print() #print a new line
print(width)

# List
fruits=["Apple", "Mango", "Banana"]
print() #print a new line
print(fruits)

# Tuple
coordinates=(1,2,3)
print() #print a new line
print(coordinates)

# Boolean
is_student = True
print() #print a new line
print(is_student)

#Dictionary
Identity={"name":"Annas", "age":26, "height": 5.8}
print() #print a new line
print(Identity)

# Set
unique_numbers={1,2,3,4,5,6}
print () #print a new line
print(unique_numbers)


# Special Keywords 
# In Python, special (reserved) keywords are words that Python already understands and uses for specific purposes.
# You cannot use them as variable or function names because Python has already assigned them a special meaning.
# Some of the keywords in Python are:
# and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.

import keyword
print() #print a new line
print(keyword.kwlist)