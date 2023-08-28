# Creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
# Modifying a value
student["age"] = 26

# Adding a new key-value pair
student["gpa"] = 3.8

print("Updated Age:", student["age"])
print("Added GPA:", student["gpa"])
# Iterating through keys
for key in student:
    print("Key:", key)

# Iterating through values
for value in student.values():
    print("Value:", value)

# Iterating through key-value pairs
for key, value in student.items():
    print(key, ":", value)
#some methods
# Checking if a key exists
if "age" in student:
    print("Age exists")

# Getting a default value for a key that might not exist
print(student.get("address", "Not available"))

# Removing a key-value pair
removed_value = student.pop("major")
print("Removed Value:", removed_value)

# Clearing all items in the dictionary
student.clear()
print("Student Dictionary:", student)
# Nested dictionary
course = {
    "name": "Python Programming",
    "instructor": {
        "name": "John Smith",
        "experience": 5
    }
}

print("Course Name:", course["name"])
print("Instructor Name:", course["instructor"]["name"])
print("Instructor Experience:", course["instructor"]["experience"])
#len
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

length = len(student)
print("Number of Key-Value Pairs:", length)
#keys,values method
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

keys_view = student.keys()
values_view = student.values()
items_view = student.items()

print("Keys:", keys_view)
print("Values:", values_view)
print("Items:", items_view)
#update method
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

new_data = {
    "age": 26,
    "gpa": 3.8
}

student.update(new_data)
print("Updated Student Dictionary:", student)
#copy method
original_dict = {"a": 1, "b": 2}
copy_dict = original_dict.copy()

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copy_dict)
#from key method
keys = ["a", "b", "c"]
default_value = 0

new_dict = dict.fromkeys(keys, default_value)
print("New Dictionary:", new_dict)
grades = {
    "Math": 90,
    "Science": 85,
    "History": 78
}
#popitem and pop method

math_grade = grades.pop("Math")
print("Math Grade:", math_grade)

last_subject = grades.popitem()
print("Last Subject:", last_subject)

