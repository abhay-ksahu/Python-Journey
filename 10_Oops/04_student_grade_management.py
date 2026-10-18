
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks < 0 or self.marks > 100:
            return "Invalid"

        elif self.marks < 40:
            return "F"

        elif self.marks < 60:
            return "D"

        elif self.marks < 75:
            return "C"

        elif self.marks < 90:
            return "B"

        else:
            return "A"

    def display(self):
        print(f"Name of student: {self.name}")

        student_grade = self.grade()

        if student_grade == "Invalid":
            print("The entered marks are not valid!")
            return

        print(f"Marks obtained: {self.marks}")
        print(f"Grade obtained: {student_grade}")

        if self.marks >= 40:
            print("Student has passed and is promoted to the next class.")
        else:
            print("Student has failed!")

name = input("Enter student name: ")
marks = int(input("Enter student marks (0-100): "))

student1 = Student(name, marks)
student1.display()
