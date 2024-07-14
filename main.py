import unittest
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

class TestClassSorting(unittest.TestCase):

    def test_sorted_students_by_lastname(self):
        sorted_students = class_5a.sorted_students_by_lastname()
        sorted_lastnames = [student.last_name for student in sorted_students]
        self.assertEqual(sorted_lastnames, ["Ежов", "Новиков", "Смирнов", "Петров"]) # Выдаст ошибку - "Смирнов" <-> "Петров"

if __name__ == "__main__":
    unittest.main()

print("Введите имя/фамилию ученика(ов):")
students_found = class_5a[input()]
if students_found:
    print("Найденный(ые) ученик(и):")
    for student in students_found:
        print(student.name, student.last_name)
else:
    print("Ученика(ов) нет в списке")