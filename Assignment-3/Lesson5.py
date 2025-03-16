# ===================== IF STATEMENTS =====================
print("===== IF STATEMENTS =====")

age = 15
if age >= 15:
    print("You are an adult")

# ELIF Statement
age = 20   
if age >= 20:
    print("You are an adult")
elif age == 18:
    print("You are a minor")
else:
    print("You are a child")

# ELSE Statement
age = 12
if age >= 18:
    print("You are an adult")  
else:
    print("You are a minor")

# NESTED IF Statements
age = 80
if age >= 15:
    print("You are an adult.")
    if age >= 75:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")


# ===================== WHILE LOOP =====================
print("\n===== WHILE LOOP =====")

counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # Increment to prevent infinite loop


# ===================== FOR LOOP WITH ELSE =====================
print("\n===== FOR LOOP WITH ELSE =====")

numbers = [10, 20, 30, 40, 50]
target = 35

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break
else:
    print(f"{target} not found in the list.")


# ===================== FOR LOOP WITH BREAK =====================
print("\n===== FOR LOOP WITH BREAK =====")

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break  # Exit loop when target is found
else:
    print(f"{target} not found in the list.")  # Won't run because of break


# ===================== FOR LOOP WITH ELSE (SEARCHING) =====================
print("\n===== FOR LOOP WITH ELSE (SEARCHING) =====")

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print(f"{target} found in the list!")
        break  # Exit loop as soon as target is found
else:
    print(f"{target} not found in the list.")  # Runs if loop finishes completely


# ===================== CONTROLLING LOOPS =====================
print("\n===== CONTROLLING LOOPS =====")

# BREAK Statement
print("\n--- Using Break ---")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop!")
        break  # Exit loop when i equals 5
    print(i)

# CONTINUE Statement
print("\n--- Using Continue ---")
for i in range(1, 10):
    if i == 5:
        print("Skipping the iteration!")
        continue  # Skip the rest of this iteration and move to next
    print(i)


# ===================== NESTED LOOPS =====================
print("\n===== NESTED LOOPS =====")

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i: {i}, j: {j}")
