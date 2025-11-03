# PYTHON LIST PRACTICE — All Important Operations (Easy → Complex)

# === EASY LEVEL ===
print("\n=== EASY LEVEL ===")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1. Accessing elements
print(fruits[0])     # apple
print(fruits[-1])    # cherry

# 2. Adding items
fruits.append("mango")
print("After append:", fruits)

# 3. Insert item at specific position
fruits.insert(1, "grape")
print("After insert:", fruits)

# 4. Removing items
fruits.remove("banana")
print("After remove:", fruits)

# 5. Pop item (remove by index)
removed = fruits.pop(2)
print("Removed:", removed)
print("After pop:", fruits)

# 6. Change item
fruits[0] = "orange"
print("After change:", fruits)

# 7. Length
print("Length:", len(fruits))

# === MEDIUM LEVEL ===
print("\n=== MEDIUM LEVEL ===")
numbers = [5, 2, 9, 1, 7, 3]
print("Numbers:", numbers)

# 1. Sorting
numbers.sort()
print("Ascending sort:", numbers)
numbers.sort(reverse=True)
print("Descending sort:", numbers)

# 2. Slicing
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Reverse list:", numbers[::-1])

# 3. Loop through list
for n in numbers:
    print("Value:", n)

# 4. Check existence
print(7 in numbers)   # True
print(10 in numbers)  # False

# 5. Count occurrences
nums = [1, 2, 2, 3, 2, 4]
print("Count of 2:", nums.count(2))

# 6. Find index of an item
print("Index of 3:", nums.index(3))

# 7. Extend list
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print("After extend:", a)

# 8. Add two lists (using +)
c = [10, 20, 30]
d = [40, 50]
e = c + d
print("After + :", e)

# === COMPLEX LEVEL ===
print("\n=== COMPLEX LEVEL ===")
data = [3, 6, 9, 12, 15, 18]

# 1. Filter even numbers
even = [x for x in data if x % 2 == 0]
print("Even numbers:", even)

# 2. Square each number
squares = [x**2 for x in data]
print("Squares:", squares)

# 3. Nested list example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix:", matrix)
print("Middle element:", matrix[1][1])   # 5

# 4. Flatten matrix using loop
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
print("Flattened:", flat)

# 5. Copy list (shallow copy)
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 6. Clear all items
fruits.clear()
print("After clear:", fruits)

# === BONUS OPERATIONS ===
print("\n=== BONUS OPERATIONS ===")
numbers = [3, 1, 4, 1, 5, 9]
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sorted (new list):", sorted(numbers))
print("Original list still:", numbers)

# === MINI PRACTICE TASKS ===
print("\n=== MINI PRACTICE TASKS ===")
nums = [10, 20, 30, 40, 50]

# 1. Print every alternate element
print(nums[::2])

# 2. Print reversed using slicing
print(nums[::-1])

# 3. Replace 30 with 35
nums[2] = 35
print(nums)

# 4. Remove last item using pop
nums.pop()
print(nums)

# 5. Add 60 and 70 at end
nums.extend([60, 70])
print(nums)

# 6. Find average
avg = sum(nums) / len(nums)
print("Average:", avg)

# 7. Create list of squares from 1–10
squares = [x**2 for x in range(1,11)]
print("Squares 1–10:", squares)

# 8. Print numbers greater than 25
for n in nums:
    if n > 25:
        print(n)

# 9. Merge two lists into a single one
x = ["a", "b", "c"]
y = [1, 2, 3]
z= [True, False, True]
merged = x + y
print("Merged:", merged)

# 10. Combine with zip
zipped = list(zip(x, y, z))
print("Zipped:", zipped)

# 11. Unzip
numbers, letters, booleans = zip(*zipped)
print("Unzipped:", numbers, letters, booleans)
