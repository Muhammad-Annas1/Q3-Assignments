
# 'w' mode: Creates a new file or overwrites if it already exists

file = open("new_file.txt", "w")

file.write("Hello, world!\n")  
file.write("This is Lesson 10 text file.\n")
file.close()

# Append new lines to the existing file using 'a' (append) mode
# 'a' mode: Adds content at the end without removing existing data

lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
file = open("new_file.txt", "a") 
file.writelines(lines)
file.close()

# Read the file content using 'r' (read) mode
# 'r' mode: Reads data from the file (file must exist)

file = open("new_file.txt", "r")
content = file.read()
print(content)  # Print the entire file content

# Trying to read one more line (but file is at the end, so nothing will be read)

line = file.readline()
print(line)

# Move the file pointer to the beginning using seek(0)

file.seek(0)
print("Position after seek(0):", file.tell())  # tell() shows current position
line = file.readline()
print(line)

# Read all lines from the file and print them

file.seek(0)  # Go to the start of file again
lines = file.readlines()
for line in lines:
    print(line)

# Another way to read the file line-by-line directly in a for loop

file = open("new_file.txt", "r")
for line in file:
    print(line.strip())  # strip() removes \n from end
file.close()

# -----------------------------
# Full Example of File Handling
# -----------------------------

# Create and write multiple lines using 'w' mode

with open('example.txt', 'w') as f:
    f.write("This is Lesson 10 text file.\n")
    f.write("This is line 2.\n")
    f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read full content at once using read()

with open('example.txt', 'r') as f:
    content = f.read()
    print("--- Full Content ---")
    print(content)

# Read file line by line using a for loop

with open('example.txt', 'r') as f:
    print("--- Line by Line ---")
    for line in f:
        print(line, end='')  # end='' prevents double line spacing

# Read only the first line

with open('example.txt', 'r') as f:
    print("\n--- Readline ---")
    print(f.readline(), end='')

# Read all lines into a list

with open('example.txt', 'r') as f:
    lines = f.readlines()
    print("\n--- Readlines ---")
    for line in lines:
        print(line, end='')

# Append more lines using 'a' mode

with open('example.txt', 'a') as f:
    f.write("This is appended line 1.\n")
    f.write("This is appended line 2.\n")

# Demonstrate seek() and tell() methods

with open('example.txt', 'r') as f:
    print("\n--- Seek and Tell ---")
    print("Current position:", f.tell())            # Show current position
    print("First line:", f.readline(), end="")      # Read one line
    print("Current position:", f.tell())            # New position after read
    f.seek(0)                                        # Move to start
    print("After seek(0):", f.tell())                # Should be 0
    print("First line again:", f.readline(), end="")  # Re-read the first line

# Try to create a file using 'x' mode (exclusive creation)
# 'x' mode: Creates file, gives error if file already exists

try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

# ---------------------
# Copy File Example
# ---------------------
def copy_file(source, destination):
    try:
        # Open source file for reading, destination file for writing

        with open(source, 'r') as src, open(destination, 'w') as dest:
            for line in src:
                dest.write(line)
            print(f"'{source}' successfully copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File not found '{source}'")
    except Exception as e:
        print(f"Error during copying: {e}")

# Call the function to copy contents from example.txt to example_copy.txt

copy_file("example.txt", "example_copy.txt")
