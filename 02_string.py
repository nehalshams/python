# Strings

print("He is called 'Johnny'")
print('He is called "Johnny"')

# assign string
a = "Hello"
print(a)


# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
  print(x)


# String Length
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)


# Slicing
# You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])


# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# Upper Case
a = "Hello, World!"
print(a.upper())


# Lower Case
a = "Hello, World!"
print(a.upper())


# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)


# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# "My name is John, I am " + age

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


# Escape Character
# To insert characters that are illegal in a string, use an escape character.
txt = "We are the so-called \"Vikings\" from the north."

# Boolean Values
print(10 > 9)
# falsy
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

