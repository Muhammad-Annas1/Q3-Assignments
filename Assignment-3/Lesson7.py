# ========== SET OPERATIONS ==========
print("===== SET OPERATIONS =====")

# Creating a Set (Unordered & Unique Elements)
my_set = {1, 2, 3, 4, 5}
print("Initial Set:", my_set)

# Adding Elements
my_set.add(6)
print("After Adding 6:", my_set)

# Removing Elements
my_set.remove(3)  # Raises error if element is not found
print("After Removing 3:", my_set)

# Unchangeable Nature (Immutable Sets)
my_set = {1, 2, 3, 4, 5, 6}
print("Unchangeable Set:", my_set)


# ========== UNIQUE ELEMENTS ==========
print("\n===== UNIQUE ELEMENTS =====")
# List with duplicate elements
elements = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# Convert to Set to Remove Duplicates
unique_elements = set(elements)
print("Unique Elements:", unique_elements)


# ========== DISCARD VS REMOVE ==========
print("\n===== DISCARD VS REMOVE =====")
my_set = {1, 2, 3, 4, 5}

# Discard an element (No error if element is missing)
my_set.discard(3)
print("After Discarding 3:", my_set)

my_set.discard(10)  # No error even if 10 is not present
print("After Discarding 10:", my_set)

# Remove an element (Raises KeyError if element is missing)
my_set = {1, 2, 3, 4, 5}

try:
    my_set.remove(3)  # Works fine
    print("After Removing 3:", my_set)

    my_set.remove(10)  # Raises error
except KeyError as e:
    print("Error:", e)


# ========== FROZEN SET OPERATIONS ==========
print("\n===== FROZEN SET OPERATIONS =====")
# Frozen Set (Immutable Set)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# Set Operations
print("Union:", fs1 | fs2)              # {1, 2, 3, 4, 5}
print("Intersection:", fs1 & fs2)        # {3}
print("Difference (fs1 - fs2):", fs1 - fs2)  # {1, 2}
print("Symmetric Difference:", fs1 ^ fs2)    # {1, 2, 4, 5}

# Membership Testing
print("Is 2 in fs1?", 2 in fs1)


# ========== GARBAGE COLLECTION ==========
print("\n===== GARBAGE COLLECTION =====")
import gc

# Trigger Garbage Collection
gc.collect()

# Get Count of Objects Collected
print("Garbage Collection Count:", gc.get_count())
