from typing import List

class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"

    def __init__(self, _homeroom_teacher, _students=None, _grade=None, _letter = None):
        self._homeroom_teacher = _homeroom_teacher
        self._students = _students if _students else []
        self._grade = _grade
        self._letter = _letter

    def __iter__(self):
        sorted_students = sorted(self._students, key=lambda student: (student.name, student.last_name))
        return iter(sorted_students)

    def __getitem__(self, name):
        filtered_students = [student for student in self._students
                             if name in student.name or name in student.last_name]
        return filtered_students

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student):
        self._students.remove(student)