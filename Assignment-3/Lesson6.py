# ========== LIST OPERATIONS ==========

print("===== LIST OPERATIONS =====")
numbers = [1, 2, 3, 4, 5]

# Accessing List Elements

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Second Last Element:", numbers[-2])


# Modifying List Elements
numbers[0] = 10
print("Updated List:", numbers)

# Adding Elements

numbers.append(6)
print("List after Appending 6:", numbers)

numbers.insert(1, 20)
print("List after Inserting 20 at index 1:", numbers)

# Removing Elements

numbers.remove(20)
print("List after Removing 20:", numbers)

last_element = numbers.pop()
print("Popped Element:", last_element)
print("List after Popping Last Element:", numbers)

# Slicing Lists

subset = numbers[1:4]  
print("Sliced List (Index 1 to 3):", subset)

# List Comprehension

squared_numbers = [x**2 for x in numbers]
print("Squared Numbers:", squared_numbers)

# Nested Lists

matrix = [[1, 2], [3, 4], [5, 6]]
print("Element at Row 1, Column 1:", matrix[1][1])


# ========== TUPLE OPERATIONS ==========

print("\n===== TUPLE OPERATIONS =====")
my_tuple = (1, 2, 3, 4, 5)

# Accessing Tuple Elements

print("First Element of Tuple:", my_tuple[0])
print("Sliced Tuple (Index 1 to 3):", my_tuple[1:3])

# Tuple Operations

tuple1 = (1, 2)
tuple2 = (3, 4)

concatenated = tuple1 + tuple2
print("Concatenated Tuple:", concatenated)

repeated = tuple1 * 3
print("Repeated Tuple:", repeated)

print("Is 3 in tuple1?", 3 in tuple1)

# Tuple Unpacking

person = ("Bilal", 20, "Khan")
name, age, surname = person
print("Unpacked Name:", name)
print("Unpacked Age:", age)
print("Unpacked Surname:", surname)


# ========== DICTIONARY OPERATIONS ==========

print("\n===== DICTIONARY OPERATIONS =====")
student = {
    "name": "Annas",
    "age": 25,
    "course": "Artificial Intelligence"
}

# Accessing Dictionary Values

print("Student Name:", student["name"])
print("Student Age:", student["age"])

# Adding a New Key-Value Pair

student["city"] = "Karachi"
print("Updated Dictionary:", student)

# Modifying Values

student["age"] = 25
print("Modified Age:", student["age"])

# Removing a Key-Value Pair

removed_value = student.pop("city")
print("Removed City:", removed_value)
print("Dictionary after Removing City:", student)

# Looping Through a Dictionary

print("Dictionary Contents:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking Key Existence

print("Is 'name' a key in dictionary?", "name" in student)

# Dictionary Comprehension

squared_numbers_dict = {x: x**2 for x in range(1, 6)}
print("Squared Numbers Dictionary:", squared_numbers_dict)
