class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        avg = sum(self.marks)/len(self.marks)
        return avg > 50

first_student = Student("Michał", [34, 46, 69, 32, 90, 59, 90, 80])
second_student = Student("Tomasz", [34, 46, 69, 32, 9, 9, 0, 11])

print(first_student.is_passed())
print(second_student.is_passed())