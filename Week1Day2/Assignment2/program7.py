class Student:

    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Student details : Name -> {self.name}, Grade -> {self.grade}, Department -> {self.department}")

    def update_grade(self, new_grade):
        self.grade = new_grade
        print("Grade of the student is updated!")

if __name__ == "__main__":
    students = [
        Student("Sunil", "10", "Engg"),
        Student("Kumar", "11", "Bio"),
        Student("Test", "12", "Testing")
    ]

    for student in students:
        student.print_info()

    students[0].update_grade("13")
    students[0].print_info()