#Arthematic Operators
print("")
print("Arthematic Operators")

a: int = 5
b: int = 2

print("a + b = ", a + b) #Addition
print("a - b= " , a - b) #Subtraction
print ("a * b = ", a * b) #Multiplication
print ("a / b = ", a / b) #Division
print ("a // b = ", a // b) #Floor division - Divides and returns the nearest whole number
print("a % b = ", a % b) #Modulus - Returns the remainder 
print ("a ** b = ", a ** b) #Exponential


#Comparison Operators
print("")
print ("Comparision Operators")

a: int = 5
b: int = 2

print ("a > b = ", a > b)
print ("a < b = ", a < b)
print ("a == b = ", a == b)
print ("a != b = ", a != b)
print ("a >= b = ", a >= b)
print ("a <= b = ", a <= b)


#Logical Operators
print("")
print ("Logical Operators")

a: bool = True
b: bool = False

print("a and b = ", a and b)
print ("a or y = " , a or b)
print ("not a = ", not a)


#Assignment Operators
print("")
print ("Assignment Operators")

x = 8
print ("Assignment: x = " , x )

x += 2
print ("Addition Assignment: x + =", x)

x -= 2
print ("Subtration Assignment: x - = ", x)

x *= 2
print ("Multiplication Assignment: x * =", x)

x /= 2
print ("Division Assignment: x / = ", x)

x //= 2
print ("Floor Assignment: x // = " , x)

#Identity operators
print ("")
print("Identity Operators")

x: list = [1,2,3]
y: list = [1,2,3]
z: list = x

print ("x is y =", x is y)
print ("x is z =", x is z)
print ("x is not y =", x is not y)
print ("x == y = ", x == y)

print('\n-----\n')

print ("id(x) =", id(x))
print ("id(y)=" , id(y))
print ("id(z) =", id(z))



#Membership Operators
print("")
print ("Membership Operators")

x = [1,2,3]
print ("1 in x =", 1 in x)
print ("4 in x =", 4 in x)
print ("1 not in x =", 1 not in x)

print('\n-----\n')

my_string: str = "Hello World"
print ("H in my_string =", "H" in my_string)
print ("h in my_string =", "h" in my_string)
print ("H not in my_string =", "H" not in my_string)


#Bitwise Operators
print("")
print ("Bitwise Operators")

a: int = 5
b: int = 2

print ("a & b = ", a & b)
print ("a | b = ", a | b)
print ("a ^ b = ", a ^ b)
print ("~a = ", ~a)
print ("a << 2 = ", a << 2)
print ("a >> 2 = ", a >> 2)


print ("")
print("Special keywords") 
import keyword
print(keyword.kwlist)




