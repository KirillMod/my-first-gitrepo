from Human import Human
from Teacher import Teacher
from Student import Student
from Subject import Subject
from enum import Enum
from typing import List


class Class(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"


    def __init__(self, _homeroom_teacher, _students=None):
        self._homeroom_teacher = _homeroom_teacher
        if  _students:
            self._students = _students
        else: []

    def __iter__(self):
        sorted_students = sorted(self._students, key=lambda student: student.name)
        return iter(sorted_students)

    def __getitem__(self, name):
        filtered_students = [student for student in self._students if name in student.name]
        return filtered_students