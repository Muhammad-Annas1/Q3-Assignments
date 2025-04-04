# The Math & Date Time Calendar

# Current time
import time
ticks = time.time ()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Formatted Time
import time
localtime = time.asctime (time.localtime(time.time()) )
print ("Local current time :", localtime)

# Calendar
import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)

# Date Time
from datetime import date

date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)

import datetime
x= datetime.datetime.now()
print(x)

# Strftime() method which format dates and times as strings.

import datetime

x = datetime.datetime(2025, 1, 1)

print(x. strftime("%f"))
print(x. strftime("%A"))
print(x. strftime("%Y"))
print(x. strftime("%B"))

# Python math module

import math

# abs() returns the positive value of a number
print("abs(-5) = ", abs(-5))

# pow() raises the first number to the power of the second number
print ("pow(2, 3) = ", pow(2, 3))

# round() rounds a number to the given number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))

# max() returns the biggest number from the given values
print ("max(1, 2, 3, 4, 5,)= ", max(1, 2, 3, 4, 5))

# min() returns the smallest number from the given values
print ("min(1, 2, 3, 4, 5,)= ", max(1, 2, 3, 4, 5))  # (Note: This should be min, not max)

# math.sin() gives the sine of an angle (in radians)
print ("math.sin (math.pi/2)=", math.sin (math.pi/2))

# math.cos() gives the cosine of an angle (in radians)
print("math.cos(0) = ", math.cos(0))  

# math.tan() gives the tangent of an angle (in radians)
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))

# math.log() returns the natural log (base e) of a number
print("math.log(10) = ", math.log(10))  

# math.log10() returns the log base 10 of a number
print("math.log10(100) = ", math.log10(100))  

# math.exp() gives e raised to the given power
print("math.exp(2) = ", math.exp(2))  

# math.ceil() returns the smallest whole number greater than or equal to the given number
print("math.ceil(4.7) = ", math.ceil(4.7)) 

# math.floor() returns the largest whole number less than or equal to the given number
print("math.floor(4.7) = ", math.floor(4.7))  

# math.pi is a constant for the value of pi (π)
print("math.pi = ", math.pi) 

# math.e is a constant for the base of natural logarithms
print("math.e = ", math.e)  

# math.tau is a constant equal to 2π (used in math with circles)
print("math.tau = ", math.tau)  

# math.inf represents positive infinity
print("math.inf = ", math.inf) 

# math.nan represents "Not a Number" (undefined value)
print("math.nan = ", math.nan)  


# NaN stands for "Not a Number"

import math

x = float ("Nan")
if math.isnan(x):
    print("x is NaN")


 # NaN compares unequal to any number, including itself. So, NaN == NaN is False

x = float('nan')
y = float('nan')

print( x == y) 

#  math.inf represents positive infinity, and it is indeed displayed as inf when you print it.

import math

positive_infinity = math.inf

print (positive_infinity)
print (type(positive_infinity))

# math.inf is a floating-point value, not an integer.

import math

positive_infinity_1 = math.inf

positive_infinity_2 = math.inf

print(positive_infinity_1 - positive_infinity_2)
print(positive_infinity_1 * 2)



import math

positive_infinity = math.inf
print(positive_infinity > 999999999999999999999999)


