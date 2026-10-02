student = {
    "name": "Abhay",
    "age": 18,
    "branch": "AIDS",
    "batch": 1,
    "college": "TCET"
}

if "marks" not in student:
    print("Data not found")

print(student.get("marks", "Not found"))
