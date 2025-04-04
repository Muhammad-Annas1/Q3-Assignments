
def perform_division():
    try:
        # Ask user to enter two numbers
        num1 = int(input("Enter the numerator (integer): "))
        num2 = int(input("Enter the denominator (integer): "))
        
        # Try to divide the numbers
        result = num1 / num2
    
    except ValueError:
        # Runs if user enters something that's not an integer
        print("Error: Invalid input! Please enter integers.")
    
    except ZeroDivisionError:
        # Runs if the user tries to divide by zero
        print("Error: Division by zero is not allowed.")
    
    else:
        # Runs only if no errors happened above
        print(f"The result of {num1} divided by {num2} is {result}.")
    
    finally:
        # Runs no matter what — used for clean-up
        print("Execution of the division operation is complete.")



# Call the function to perform the division
perform_division()


def process_file(file_name):
    try:
        # Try to open and read the file
        with open(file_name, 'r') as file:
            data = file.read()
            # Check if the file is empty
            if len(data) == 0:
                raise ValueError("The file is empty!")
            print("File content successfully read.")
            print("Processing data...")
            # Try converting the file data to an integer
            processed_data = int(data.strip())
            print(f"Processed data: {processed_data}")
        
    except FileNotFoundError:
        # Runs if the file was not found
        print(f"Error: The file '{file_name}' was not found.")
    
    except ValueError as ve:
        # Runs if file content is invalid
        print(f"Error: {ve}")
    
    except Exception as e:
        # Catches any other unexpected error
        print(f"An unexpected error occurred: {e}")
    
    else:
        # Runs only if no errors occurred
        print("File processed successfully, no errors.")
    
    finally:
        # Always runs — useful for cleanup
        print("File processing complete. Cleanup actions done.")

# Ask user to enter the file name
file_name = input("Enter the name of the file to process: ")

# Call the function with the file name
process_file(file_name)


# This function shows different examples of how errors are handled in Python.
def error_handling_demo():
    print("Welcome to the Python Error Handling Demo!\n")
    
    # 1. Simple try-except example
    try:
        x = 5 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    
    print("\n---\n")

    # 2. Handling multiple specific types of errors
    try:
        num = int(input("Enter a number to divide 100 by: "))
        result = 100 / num
        print(f"100 divided by {num} is {result}.")
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    print("\n---\n")

    # 3. Using 'else' when no error happens
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input! Please enter integers.")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    
    print("\n---\n")

    # 4. Using 'finally' for cleanup
    try:
        print("Opening a file for reading...")
        file = open("sample.txt", "r")  # Try opening a file
        content = file.read()
        print("File content read successfully.")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        # Always close the file if it was opened
        try:
            file.close()
            print("File is closed.")
        except NameError:
            # If file never opened, skip closing
            print("No file to close.")
    
    print("\n---\n")

    # 5. Catching any unexpected errors using Exception
    try:
        number = int(input("Enter a number to square: "))
        if number < 0:
            raise Exception("Negative numbers are not allowed!")
        print(f"The square of {number} is {number**2}.")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n---\n")

    # 6. Manually raising an error
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise ValueError("You must be at least 18 years old.")
        print(f"Your age is {age}. You are eligible!")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    print("\n---\n")

    # 7. Using else when there's no error
    try:
        num1 = int(input("Enter a number to double: "))
        result = num1 * 2
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
    else:
        print(f"The doubled value is: {result}.")
    
    print("\n---\n")

# Call the function to run all the demos
error_handling_demo()


# Function that does not return anything
def no_return():
    print("This function doesn't return anything.")

result = no_return()  # result will be None
print(result)  # Output: None

# The function no_return doesn't have a return statement, so it returns None by default


# Function that always raises an error or never returns
from typing import NoReturn

def raise_error() -> NoReturn:
    raise ValueError("Something went wrong!")

def infinite_loop() -> NoReturn:
    while True:
        pass  # Infinite loop, never ends


# Function with no return type hint
def no_return_type():
    print("This function has no return type hint.")
