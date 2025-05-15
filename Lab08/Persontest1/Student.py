from Person import Person

class Student(Person):
    def __init__(self, name, address, age, major, units_completed):
        super().__init__(name, address, age)
        self.__major = major
        self.__units_completed = units_completed

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major

    def get_units_completed(self):
        return self.__units_completed

    def set_units_completed(self, units_completed):
        self.__units_completed = units_completed

    def to_string(self):
        person_info = super().to_string()
        return f"{person_info}, Major: {self.__major}, Units Completed: {self.__units_completed}"



