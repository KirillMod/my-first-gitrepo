from Teacher import Teacher
from Student import Student
from Subject import Subject
from Class import Class


subjects = [Subject.MATH, Subject.CHEM, Subject.LITER]

teacher = Teacher("Иван", "Иванов", subjects)

student1 = Student("Иван", "Смирнов")
student2 = Student("Петр", "Петров")
student3 = Student("Александр", "Ежов")

class_1a = Class(teacher, [student1, student2, student3])

print("Список учеников по алфавиту:")
for student in class_1a:
    print(f"{student.name} {student.last_name}")