# STRING SLICING PRACTICE - Easy, Medium, Complex, Bonus

text = "Artificial"
print("Original text:", text)

# print("\n=== EASY LEVEL ===")
# print(text[0])          # 'A' → first letter
# print(text[-1])         # 'l' → last letter
# print(text[0:5])        # 'Artif' → from index 0 up to 5 (not included)
# print(text[:4])         # 'Arti' → from start to 4
# print(text[4:])         # 'ficial' → from index 4 till end
# print(text[:])          # 'Artificial' → full copy

# print("\n=== MEDIUM LEVEL ===")
# print(text[-4:])        # 'cial' → last 4 chars
# print(text[:-4])        # 'Artifi' → everything except last 4
# print(text[-1:-5:-1])   # 'laic' → reverse last 4 letters
# print(text[::-1])       # 'laicifitrA' → full reverse
# print(text[-3:-8:-1])   # 'icifi' → reverse from -3 to -8

# print("\n=== COMPLEX LEVEL ===")
# text = "Artificial Intelligence"
# print("New text:", text)
# print(text[0:10:2])     # 'Atfca' → every 2nd char till index 10
# print(text[::3])        # 'Aiclnlgc' → every 3rd char
# print(text[::-2])       # 'englen acftA' → reverse skipping every 2nd
# print(text[5:1:-1])     # 'ifit' → reverse slice from 5 to 1
# print(text[-10:-1:2])   # 'tliec' → from -10 to -1 jumping by 2

# print("\n=== BONUS TASKS ===")
# # 1. Reverse last 5 characters only
# print(text[-1:-6:-1])   # last 5 reversed

# # 2. Print middle part (6 letters around center)
# mid = len(text)//2
# print(text[mid-3:mid+3])

# # 3. Extract word “Intel”
# print(text[11:16])

# # 4. Reverse only first word
# first_word = text.split()[0]
# print(first_word[::-1])

print("\n=== MINI PRACTICE QUESTIONS ===")
t = "Artificial Intelligence"
print("Text:", t)
# 1. Print last 5 letters
print("1:", t[-5:])
# 2. Print first 3 letters
print("2:", t[:3])
# 3. Print everything except first and last letter
print("3:", t[1:-1])
# 4. Reverse entire string
print("4:", t[::-1])
# 5. Print characters from index 3 to 10
print("5:", t[3:10])
# 6. Print from -5 to -10 in reverse
print("6:", t[-5:-11:-1])
# 7. Print every 2nd character in reverse
print("7:", t[::-2])
print("=== END OF PRACTICE ===")


# Additional slicing tests tricky cases
print("\n=== ADDITIONAL SLICING TESTS ===")
print(text[-5:-5:-1]) # empty string
print(text[-5:-8:-1]) # 'ila'
print(text[-5:-8:1]) # empty string
print(text[-5:8:1])