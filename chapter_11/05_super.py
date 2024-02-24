class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath() # by use of super method it also prints the same function of it's super(base) class
        # if it's super class don't contains the same method then it go 1 step more(dadaji) to get method and so on..
        # and if no one would contain till the 1st base class then it shows error
        print("I am a programmer so I am breathing... more than you")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()