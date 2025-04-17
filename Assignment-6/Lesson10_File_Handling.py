# File handling example with "Write"

with open("file.txt", "w", encoding="utf-8") as file:
          file.write("Hello Annas!👋 \n")
          file.write("Welcome to Python Programming!👍")


# File handling example with "Read"

with open ("file.txt", "r" , encoding="utf-8") as file:
          content = file.read()
          print(content)

# User input and append in file

message = input("Hello Annas!👋 \nWelcome to Python Programming!👍 ")

with open("messages.txt", "a", encoding="utf-8") as file:
    file.write(message + "\n")

print("Message saved to messages.txt successfully! ✅")