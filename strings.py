a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
for x in "banana":
  print(x)
#len
a = "Hello, World!"
print(len(a))
#check string
txt = "The best things in life are free!"
print("free" in txt)
#string concatnation
b=" your name"
a="hello"+b
print(a)
#string slicing
#very simillar to list slicing
b = "Hello, World!"
print(b[2:5])
word = "Python"
print(word[0:3])    # Output: "Pyt"
print(word[2:])     # Output: "thon"
print(word[::-1])   # Output: "nohtyP" (reversed)
#escape sequences
print("Line 1\nLine 2")
print("Tabbed\tText")
print("Backslash: \\")
#string methods
text = "Hello, World"
print(text.upper())       # Output: "HELLO, WORLD"
print(text.startswith("H"))  # Output: True
print(text.replace("World", "Python"))  # Output: "Hello, Python"
#split
sentence = "Hello, how are you?"
words = sentence.split()
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']
#join
words = ['Hello', 'how', 'are', 'you?']
sentence = ' '.join(words)
print(sentence)  # Output: "Hello how are you?"
#strip
text = "   spaces   "
trimmed = text.strip()
print(trimmed)  # Output: "spaces"
#lower and upper
message = "Hello, World"
lower_case = message.lower()
upper_case = message.upper()
#find
text = "Hello, World"
index = text.find("World")
print(index)  # Output: 7
#count
text = "How much wood would a woodchuck chuck?"
count = text.count("wood")
print(count)  # Output: 2

