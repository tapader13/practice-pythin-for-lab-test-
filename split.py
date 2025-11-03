# STRING SPLIT() PRACTICE - Easy, Medium, Complex

text = "I love Artificial Intelligence"
print("Original text:", text)

print("\n=== EASY LEVEL ===")

# 1. Default split by spaces
words = text.split()
print(words)
# ['I', 'love', 'Artificial', 'Intelligence']

# 2. Access individual words
print(words[0])     # I
print(words[-1])    # Intelligence
print(len(words))   # total words

# 3. Loop through each word
for w in words:
    print("Word:", w)

print("\n=== MEDIUM LEVEL ===")

# 4. Split by a specific character
text2 = "apple,banana,mango,grape"
fruits = text2.split(",")
print(fruits)
# ['apple', 'banana', 'mango', 'grape']

# 5. Split by colon :
info = "Name:Minhaj:Dept:AI"
parts = info.split(":")
print(parts)

# 6. Split and pick certain parts
print("Name:", parts[1])
print("Department:", parts[-1])

# 7. Limit number of splits
text3 = "I love Python and AI and ML"
print(text3.split("and", 1))  # split only once

print("\n=== COMPLEX LEVEL ===")

# 8. Split by spaces then join back with '-'
text4 = "Data Science is powerful"
words = text4.split()
joined = "-".join(words)
print(joined)  # Data-Science-is-powerful

# 9. Split string into characters (using list)
chars = list(text4)
print(chars)

# 10. Combine split() + slicing
sentence = "Machine Learning is fun"
parts = sentence.split()
print("Reversed last two words:", parts[-1::-1])

# 11. Remove extra spaces
messy = "   Hello   AI   World   "
cleaned = messy.strip()        # remove spaces at start/end
words = cleaned.split()        # split by spaces
print(words)

# 12. Split a sentence and print each word in uppercase
for word in text.split():
    print(word.upper())

print("\n=== MINI PRACTICE TASKS ===")
# Try to predict outputs before running
text = "Python is fun to learn"
print(text.split(" "))        # 1. Split by space
print(text.split("is"))       # 2. Split by 'is'
print(text.split("n"))        # 3. Split by 'n'
print(text.split("o"))        # 4. Split by 'o'
print("-".join(text.split())) # 5. Join words with '-'

# BONUS: Count number of words
print("Word count:", len(text.split()))

# BONUS 2: Split and print words longer than 3 letters
for w in text.split():
    if len(w) > 3:
        print(w)
