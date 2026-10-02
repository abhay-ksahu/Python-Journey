# MAX AND MIN 
student = {
    "python": 99,
    "java": 95,
    "c++": 98
}

# higest = max(student.values())
# print(higest)

higest = max(student, key=student.get) 
print(higest)