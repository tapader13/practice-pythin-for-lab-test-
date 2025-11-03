# Tuple Basics and Operations Practice

# Creating tuples
t1 = (1, 2, 3, 4, 5)
t2 = ("AI", "ML", "DL")
t3 = (10, 20, 30, 40, 50, 60)

print("t1:", t1)
print("t2:", t2)
print("Length of t1:", len(t1))
print()

# Accessing elements
print("First element:", t1[0])
print("Last element:", t1[-1])
print("Middle 3 elements:", t3[1:4])  # slicing
print()

# Slicing (forward & backward)
print("t3[2:5]:", t3[2:5])      # (30, 40, 50)
print("t3[::-1]:", t3[::-1])    # reverse the tuple
print("t3[-1:-4:-1]:", t3[-1:-4:-1])  # (60, 50, 40)
print()

# Tuple concatenation
t4 = t1 + t2
print("Concatenation:", t4)
print()

# Tuple repetition
t5 = t2 * 2
print("Repetition:", t5)
print()

# Membership test
print("Is 3 in t1?", 3 in t1)
print("Is 'Python' in t2?", 'Python' in t2)
print()

# Iterating through a tuple
for item in t2:
    print("Item:", item)
print()

# Tuple unpacking
a, b, c = t2
print("Unpacked values:", a, b, c)
print()

# Nesting tuples
nested = (t1, t2)
print("Nested tuple:", nested)
print("Accessing inside nested tuple:", nested[0][2])  # 3
print()

# Using built-in functions
nums = (4, 2, 9, 1, 7)
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted (returns list):", sorted(nums))
print()

# Count & Index
print("Count of 2 in nums:", nums.count(2))
print("Index of 9:", nums.index(9))
print()

# Type conversion
list_from_tuple = list(t1)
print("Tuple → List:", list_from_tuple)

tuple_from_list = tuple(list_from_tuple)
print("List → Tuple:", tuple_from_list)
print()

# Deleting tuple (only entire tuple can be deleted)
temp = (1, 2, 3)
print("Before delete:", temp)
del temp
# print(temp)  # Error: tuple is deleted
