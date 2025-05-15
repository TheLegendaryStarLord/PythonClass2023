from Person import Person

class Employee(Person):
    def __init__(self, name, address, age, job_skills, years_worked):
        super().__init__(name, address, age)
        self.__job_skills = job_skills
        self.__years_worked = years_worked

    def get_job_skills(self):
        return self.__job_skills

    def set_job_skills(self, job_skills):
        self.__job_skills = job_skills

    def get_years_worked(self):
        return self.__years_worked

    def set_years_worked(self, years_worked):
        self.__years_worked = years_worked

    def to_string(self):
        person_info = super().to_string()
        return f"{person_info}, Job Skills: {self.__job_skills}, Years Worked: {self.__years_worked}"

