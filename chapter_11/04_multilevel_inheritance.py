class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

p = Person()
e = Employee()
pr = Programmer()

pr.takeBreath() # so it is taking the method or attribute of the class from which it is inherit or derived not of that class which is base class of it's base class
# means the child class is using the methods and attributes of (papaji) class not (dadaji) class 