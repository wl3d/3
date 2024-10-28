class Student:
    def __init__(self, first_name, last_name, birth_date, height=160, school="", grade=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.height = height
        self.school = school
        self.grade = grade

    def __bool__(self):
        return bool(self.school)

    def __float__(self):
        return float(self.grade)

first_student = Student("Ivan", "Ivanov", "12.02.2010", 186, "School #1", grade=11)
second_student = Student("Petr", "Petrov", "28.06.2009", 220, grade=10)

print(first_student.first_name, first_student.last_name, first_student.birth_date, first_student.height, first_student.school, float(first_student.grade))
print(bool(first_student))
print(second_student.first_name, second_student.last_name, second_student.birth_date, second_student.height, second_student.school, float(second_student.grade))
print(bool(second_student))
