import json
import os

students = {}
next_student_number = 1

FILE_NAME = "students.json"


def load_students():
    global students, next_student_number

    if not os.path.exists(FILE_NAME):
        students = {}
        next_student_number = 1
        return

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        students = {
            int(number): student
            for number, student in data.get("students", {}).items()
        }

        next_student_number = max(students.keys(), default=0) + 1

        print(f"Loaded {len(students)} student record(s).")

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Could not load student records: {error}")
        students = {}
        next_student_number = 1


def save_students():
    data = {
        "students": students
    }

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except OSError as error:
        print(f"Could not save student records: {error}")


def get_student_by_id(student_id):
    for number, student in students.items():
        if student["ID"] == student_id:
            return number, student

    return None, None


def add_student():
    global next_student_number

    try:
        count = int(input("How many students do you want to add? "))

        if count <= 0:
            print("Enter a number greater than 0.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    added = 0

    for _ in range(count):
        print("\nEnter student details:")

        name = input("Student name: ").strip()

        if not name:
            print("Name cannot be empty. Student skipped.")
            continue

        student_id = input("Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty. Student skipped.")
            continue

        _, existing_student = get_student_by_id(student_id)

        if existing_student is not None:
            print("This student ID already exists. Student skipped.")
            continue

        try:
            marks = float(input("Marks (0-100): "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue

        except ValueError:
            print("Please enter valid numeric marks.")
            continue

        students[next_student_number] = {
            "name": name,
            "marks": marks,
            "ID": student_id
        }

        print(f"Student added! Number: {next_student_number}")

        next_student_number += 1
        added += 1

    if added > 0:
        save_students()

    print(f"\nSuccessfully added {added} student(s).")


def search_student():
    if not students:
        print("No students available to search.")
        return

    student_id = input("Enter student ID to search: ").strip()
    number, student = get_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent found!")
    print(f"Student number: {number}")
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Student ID: {student['ID']}")


def view_all_students():
    if not students:
        print("No student records available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for number, student in students.items():
        print(f"\nStudent number: {number}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Student ID: {student['ID']}")

    print("\n==================================")

def delete_student():
    if not students:
        print("No students available to delete.")
        return

    student_id = input("Enter student ID to delete: ").strip()
    number, student = get_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    del students[number]
    save_students()

    print(f"Student '{student['name']}' deleted successfully!")


def update_student():
    if not students:
        print("No students available to update.")
        return

    student_id = input("Enter student ID to update: ").strip()
    number, student = get_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Marks")
    print("3. Student ID")

    choice = input("Enter your choice: ").strip().lower()

    if choice in ["1", "name"]:
        new_name = input("Enter new name: ").strip()

        if not new_name:
            print("Name cannot be empty.")
            return

        student["name"] = new_name

    elif choice in ["2", "marks"]:
        try:
            new_marks = float(input("Enter new marks (0-100): "))

            if not 0 <= new_marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            student["marks"] = new_marks

        except ValueError:
            print("Please enter valid numeric marks.")
            return

    elif choice in ["3", "id", "student id"]:
        new_id = input("Enter new student ID: ").strip()

        if not new_id:
            print("Student ID cannot be empty.")
            return

        _, existing_student = get_student_by_id(new_id)

        if existing_student is not None and new_id != student["ID"]:
            print("This student ID already exists.")
            return

        student["ID"] = new_id

    else:
        print("Invalid update choice.")
        return

    save_students()
    print(f"Student details updated! Number: {number}")


load_students()

while True:
    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add student")
    print("2. Search student")
    print("3. Delete student")
    print("4. Update student")
    print("5. View all students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip().lower()

    if choice in ["1", "add", "add student"]:
        add_student()

    elif choice in ["2", "search", "search student"]:
        search_student()

    elif choice in ["3", "delete", "delete student"]:
        delete_student()

    elif choice in ["4", "update", "update student"]:
        update_student()

    elif choice in ["5", "view", "view all", "view all students"]:
        print("option 5 selected")
        view_all_students()

    elif choice in ["6", "exit"]:
        save_students()
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Select an option from 1 to 6.")
