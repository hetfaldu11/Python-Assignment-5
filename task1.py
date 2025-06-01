dict = {
    "John" : 25,
    "Peter" : 30,
    "Mike" : 35,
    "Susan" : 28,
    "Linda" : 32,
    "James" : 40,
    "Karen" : 29
}

name = input("Enter the student's name: ")

if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("Student not found.")