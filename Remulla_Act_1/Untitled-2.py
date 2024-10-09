class Person:
    def __init__(self):
        self.name= input("Enter your name: ")
        self.student_ID= int (input("Enter your student ID: "))

class Student(Person):
    def __init__(self):
        super().__init__()
        self.course= input("Enter your course: ")
        self.section= input("Enter your section: ")

class GradeAverage:
    def __init__ (self):
        self.prelim = self.get_valid_grade("Enter your Prelim Grade: ")
        self.midterm = self.get_valid_grade("Enter your Midterm Grade: ")
        self.final = self.get_valid_grade("Enter your Final Grade: ")

    def get_valid_grade(self, prompt):
        while  True:
            grade = int(input(prompt))
            if  0 <= grade <=100:
                return grade
            print("Invalid grade")

    def calculate_average (self):
        average= (self.prelim + self.midterm + self.final) / 3
        return average

    def check_pass_fail(self):
        final_average = self.calculate_average()
        if final_average >= 75:
            print("RESULT PASSED")
        else:
            print("FAILED")

class Student1(Student, GradeAverage):
    def __init__(self):
        Student.__init__(self)
        GradeAverage.__init__(self)

    def display_info(self):
        print("\nStudent Information and Final Grade \n")
        print("--- Student Information ---")
        print(f"Student name: {self.name}")
        print(f"Student ID: {self.student_ID}")
        print(f"Course: {self.course}")
        print(f"Section: {self.section} ")
        print(f"Grade Average: {self.calculate_average()}")
        print(f"Result: {self.check_pass_fail}")


Student= Student1()
Student.display_info()



















