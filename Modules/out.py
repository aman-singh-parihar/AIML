def print_information():
    print("Print information")

name = "child-modules"

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def get_student_details(self):
        print("Your name is "+self.name)
        print("Your course is "+self.course)