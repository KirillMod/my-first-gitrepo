from Human import Human
from Class import Class

class Student(Human):
    _class: Class

    def __init__(self, name: str, last_name: str, _class=None):
        super().__init__(name, last_name)
        self._class = _class

    def set_class(self, new_class):
        self._class = new_class

    def get_class(self):
        return self._class