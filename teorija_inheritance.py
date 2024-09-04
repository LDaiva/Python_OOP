# Inheritance - paveldejimas

# Employee
class Employee:
    def __init__(self, name, age, experience, salary):
        self.name = name
        self.age = age
        self.experiece = experience
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.experiece, self.salary)


class Engineer(Employee):
    def __init__(self, name, age, experience, salary, programming_language):
        super().__init__(name, age, experience, salary)
        self.programming_language = programming_language


eng = Engineer('Adas', 22, 1, 2000,'Python')
print(eng.programming_language)
print(eng.show())
eng.show()
print(eng.name)
print(eng.age)
print(eng.experiece)
print(eng.salary)

class Designer(Employee):
    def __init__(self, name, age, experience, salary, programming):
        super().__init__(name, age, experience, salary)
        self.programming = programming

    def show(self):
        super().show()
        print(f'Vaikines klases Designer isplesta show f-ja: {8+8}')


des = Designer('Tadas', 30, 10, 2500,'Figma')
print(des.programming)
print(des.show())
des.show()
print(des.name)
print(des.age)
print(des.experiece)
print(des.salary)


