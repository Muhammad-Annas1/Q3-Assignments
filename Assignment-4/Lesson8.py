# Modules in python

# Built-in modules
import math
print (math.sqrt(25))

# User-defined modules
import mymodule
print(mymodule.add(5,3))


import math
print(math.pi)

import numpy as np
print(np.array([1, 2, 3]))

from math import sqrt,pi
print(sqrt(16))
print(pi)

from math import *
print(sin(0))

# Functions in python

# User-defined functions
# Built-in functions
print ("Hello! World")

# Functions defined in built-in modules
import random
print(random.random())

# User-defined functions
def my_function():
    print("Hello! Operation Badar")

my_function()

# Syntax to define a python function

def greetings():
   "This is docstring of greetings function"
   greet = 'Hello World!'
   return greet

message = greetings()
print(message)

# Pass by reference vs value

def modify_value(x):
    x = 10
    print("Within function:", x)

# Immutable object (integer)
x = 5
print("Original:" , x)
modify_value(x)
print("After function", x)

def modify_list(lst):
    lst.append(4)
    print("Within function: ", lst, " - ID:", id(lst))

# Mutable object (list)
lst = [1, 2, 3]
print("Original:", lst, " - ID:", id(lst))
modify_list(lst)
print("After function:", lst, " - ID:", id(lst))

# Function arguments
def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return

greetings("Annas")
greetings("Alishba")
greetings("Hesham")

# Keyword arguments
def printinfo (name,age):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;

printinfo( age=50, name="Arif" )

# Float argument

def add(x: int,y: int=0) -> float:
   return float(x + y)

print(float(add(10,20)))

print(add(y=50.0, x=2.0)) 
print(add(x=5))

# Default arguments

def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

printinfo( age=50, name="Arif" )
printinfo( name="Arif" )

# Keyword- only arguments

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5)

posFun(num3=6, num1=8, num2=5)

# Function with return value

def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)

print ("a = {} b = {} a+b = {}".format(a, b, result))

# Anonymous functions

def add_two (x, y):
    return x + y

my_lambda = lambda x, y: x + y;

print (my_lambda (1,2))

# Generator function

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(gen, " : ", type(gen))


for value in gen:
    print(value, " : ", type(value))

# Recursive function

def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
number = 5
result = factorial (number)
print (f"The factorial of {number} is {result}")

# Infinite sequence

def infinite_sequence():
    num = 0
    while True:
        yield num 
        num += 1

gen = infinite_sequence()

for _ in range (5):
    print (next(gen))


# Fibonacci sequence

def fibonacci(n):

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6)) 


# Multi type return in function
from typing import Tuple, List, Dict

def example_function(a: int, b: int = 0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
    """Example function demonstrating various parameter types.
    Args:
        a: An integer.
        b: An integer with a default value of 0.
        *args: Variable-length positional arguments of type float.
        **kwargs: Variable-length keyword arguments of type string.
    Returns:
        A tuple containing:
        - The sum of 'a' and 'b'.
        - A list of the variable-length positional arguments ('args').
        - A dictionary of the variable-length keyword arguments ('kwargs').
    """
    sum_ab = a + b
    args_list = list(args)  
    return sum_ab, args_list, kwargs


result1 = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result1)

result2 = example_function(10, *[1.0, 2.0, 3.0], **{"country": "USA", "language": "English"})
print(result2)

















