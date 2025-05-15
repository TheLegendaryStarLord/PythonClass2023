
from employee import Employee
from Student import Student

# Input for an employee
name = input("Enter name: ")
address = input("Enter address: ")
age = int(input("Enter age: "))
skills = input("Enter job skills: ")
years_worked = int(input("Enter years worked: "))
major = input("Enter student major: ")
units_completed = int(input("Enter units completed: "))

# Create instances of Employee and Student
employee = Employee(name, address, age, skills, years_worked)
student = Student(name, address, age, major, units_completed)

# Display the information
print("Employee Info:")
print(employee.to_string())

print("\nStudent Info:")
print(student.to_string())

