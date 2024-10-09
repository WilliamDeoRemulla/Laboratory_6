class Person:
    def __init__(self):
        self.name = input("Name: ")
        self.student_id = input("Student ID: ")

class Student(Person):
    def __init__(self):
        super().__init__()
        self.course = input("Course: ")
        self.section = input("Section: ")

class GradeAverage:
    def __init__(self):
        self.grades = [self.get_valid_grade(exam) for exam in ["Prelim", "Midterm", "Finals"]]

    def get_valid_grade(self, exam):
        while True:
            try:
                grade = float(input(f"{exam} grade (0-100): "))
                if 0 <= grade <= 100: return grade
                print("Error: Must be 0-100.")
            except ValueError:
                print("Error: Invalid input.")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def check_pass_fail(self, average):
        return "Passed" if average >= 75 else "Failed"

class Student1(Student, GradeAverage):
    def __init__(self):
        Student.__init__(self)
        GradeAverage.__init__(self)

    def display_info(self):
        avg = self.calculate_average()
        print(f"\n--- Info ---\nName: {self.name}\nID: {self.student_id}\nCourse: {self.course}\nSection: {self.section}\nAverage: {avg:.2f}\nResult: {self.check_pass_fail(avg)}")

# Create instance and display info
student = Student1()
student.display_info()


class Person:
    def __init__(self):
        self.name = input("Name: ")
        self.employeeID = int(input("ID: "))

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.department = input("Department: ")
        self.position = input("Position: ")

    def print_info(self):
        print(f"Dept: {self.department}, Pos: {self.position}")

class Salary:
    def __init__(self):
        self.wage_per_hour = float(input("Wage: "))
        self.hours_per_day = int(input("Hours/day: "))
        self.total_days = int(input("Days/month: "))

    def calculate_total_salary(self):
        return self.wage_per_hour * self.hours_per_day * self.total_days

def display_salary_info(total_salary):
    return f"Salary: ${total_salary:.2f}"

class Employee1(Employee, Salary):
    def __init__(self):
        Employee.__init__(self)
        Salary.__init__(self)

    def display_info(self):
        print(f"{self.name}, ID: {self.employeeID}")
        self.print_info()
        print(display_salary_info(self.calculate_total_salary()))

employee1 = Employee1()
employee1.display_info()
