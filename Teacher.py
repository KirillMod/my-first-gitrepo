class Teacher(Human):
    _homeroom_class: Class | None
    _subjects: List[Subject]

    def __init__(self, name: str, last_name: str, _subjects):
        super().__init__(name, last_name)
        self._subjects = _subjects

    def set_class(self, new_class):
        self._homeroom_class = new_class

    def get_class(self):
        return self._homeroom_class