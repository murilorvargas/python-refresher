class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
        
student = Student("Rolf", (89, 90, 93, 78, 90))

print(Student.average_grade(student))
print(student.average_grade())
