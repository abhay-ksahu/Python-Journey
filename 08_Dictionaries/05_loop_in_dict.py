student = {
    "name": "Abhay",
    "age": 18,
    "branch": "AIDS",
    "batch": 1,
    "college": "TCET"
}

for info in student.keys():
    print(info)

for info in student.values():
    print(info)

for keys, values in student.items():
    print(keys,"=",values)