# PYTHON DICTIONARY PRACTICE — All Operations in One Box

# === BASIC DICTIONARY ===
print("\n=== BASIC DICTIONARY ===")
student = {
    "name": "Minhaj",
    "age": 21,
    "course": "AI"
}
print("Original dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding/Updating items
student["age"] = 22          # Update existing
student["grade"] = "A"       # Add new key-value
print("After update/add:", student)

# Deleting items
del student["course"]        # Delete key
print("After deleting 'course':", student)
removed = student.pop("grade")  # Removes and returns value
print("Removed grade:", removed)
print("Dictionary now:", student)

# Length
print("Number of keys:", len(student))

# === MEDIUM LEVEL ===
print("\n=== MEDIUM LEVEL ===")
# Looping
for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, "->", value)

# Keys and Values
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Check existence
print("Is 'name' in student?", "name" in student)
print("Is 'course' in student?", "course" in student)

# Copy dictionary
student_copy = student.copy()
print("Copied dict:", student_copy)

# Clear dictionary
temp = student_copy.copy()
temp.clear()
print("After clear:", temp)

# === COMPLEX / NESTED DICTIONARY ===
print("\n=== NESTED DICTIONARY ===")
students = {
    "s1": {"name": "Minhaj", "age": 21},
    "s2": {"name": "Rina", "age": 22},
    "s3": {"name": "Arif", "age": 20}
}
print("Nested dictionary:", students)

# Access nested value
print("s2's name:", students["s2"]["name"])

# Update nested value
students["s3"]["age"] = 21
print("After update s3 age:", students)

# Add nested value
students["s1"]["course"] = "AI"
print("After adding course to s1:", students)

# Loop nested dictionary
for student_id, info in students.items():
    print(student_id, "info:")
    for key, value in info.items():
        print("   ", key, "->", value)

# === DICTIONARY METHODS & FUNCTIONS ===
print("\n=== DICTIONARY METHODS ===")
info = {"a": 10, "b": 20, "c": 30}

# get()
print("Value of 'a':", info.get("a"))
print("Value of 'z' (default 0):", info.get("z", 0))

# popitem()
last = info.popitem()   # Removes last inserted item
print("Popped item:", last)
print("After popitem:", info)

# fromkeys()
keys = ["x", "y", "z"]
default_dict = dict.fromkeys(keys, 0)
print("fromkeys:", default_dict)

# setdefault()
d = {"a": 1}
d.setdefault("b", 2)    # Adds 'b' if not present
d.setdefault("a", 100)  # Does not change existing 'a'
print("After setdefault:", d)

# update()
d.update({"a": 10, "c": 3})  # Update existing + add new
print("After update:", d)

# === BONUS TASKS ===
print("\n=== BONUS TASKS ===")
# 1. Merge two dictionaries
x = {"p": 1, "q": 2}
y = {"q": 10, "r": 3}
x.update(y)
print("Merged dict:", x)

# 2. Get max and min value
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Max value:", max(squares.values()))
print("Min value:", min(squares.values()))


