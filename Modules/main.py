#example 1
import out
out.print_information()
print(out.name)
student = out.Student("Aman","CS")
student.get_student_details()

#example 2
from out import print_information
print_information()

#example 3
from out import *
print_information()
student2 = Student("Aman","Engineering")
student2.get_student_details()