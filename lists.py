#list slicing
"""
a=[]
b=int(input("please enter how many elements you need: "))
for i in range(b):
    a.append(i+1)
print(a[1:2])
print(a[0:9:2])
print(a[::-1])
print(a[8::-2])
"""
#changing list elements
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
"""

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
"""
#iterating through the list
for i in thislist:
    print(f"Hi would you like to have {i}")
    choice=input("Please enter yes or no: ")
    if(choice==("yes"or"Yes"or"yES"or"yEs"or"yeS")):
        print("order recieved")
        break
    else:
        print("okay printing next menu item")
fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
print(fruits)  # Output: ["apple", "banana", "cherry", "grape"]
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Output: []
original = [1, 2, 3]
copied = original.copy()
print(copied)  # Output: [1, 2, 3]
fruits = ["apple", "banana", "apple", "cherry"]
count = fruits.count("apple")
print(count)  # Output: 2
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # Output: 1
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)  # Remove and return "banana"
print(removed_fruit)  # Output: "banana"
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ["apple", "cherry"]
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

    