from Teacher import Teacher
from Student import Student
from Subject import Subject
from Class import Class


subjects = [Subject.MATH, Subject.CHEM, Subject.LITER]

teacher = Teacher("Иван", "Иванов", subjects)

student1 = Student("Иван", "Смирнов")
student2 = Student("Петр", "Петров")
student3 = Student("Александр", "Ежов")
student4 = Student("Александр", "Новиков")

class_5a = Class(teacher, [student1, student2, student3, student4], 5, "А")

print(f"Класс {class_5a._grade}{class_5a._letter}, классный руководитель: {class_5a._homeroom_teacher.name} {class_5a._homeroom_teacher.last_name}")
print("Список учеников по алфавиту:")
for student in class_5a:
    print(f"{student.name} {student.last_name}")

print("Введите имя/фамилию ученика(ов):")
students_found = class_5a[input()]
for student in students_found:
    print(student.name, student.last_name)