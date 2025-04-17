correct_password = "AnnasGiaic"

try:
    password = input("Enter your password: ")
    if password != correct_password:
        raise ValueError("Wrong password!")
except ValueError as e:
    print("❌", e)
    print("Login attempt failed!⚠️")

else:
    print("Access granted!✅")
   

finally:
    print("login attempt done.🔚")



try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result = a/b
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You cannot use non-numeric characters!")
else:
    print(result)
finally:
    print(" End of division, Done✅")