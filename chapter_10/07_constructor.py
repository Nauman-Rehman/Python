class Employee:
    company = "Google"

    def __init__(self): # it is a constructor and have been called automatically when an object in initialize, it only have name (__init__)
        print("Employee is created")

    def __init__(self, name, salary, submit): # here we have make a new constructor so from now the old one will not work  
        self.name = name
        self.salary = salary
        self.company = submit
        print(f"The name of the employee is {self.name}")
        print(f"His salary is {self.salary}")
        print(f"His company is {self.company}")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"His salary is {self.salary}")
        print(f"His company is {self.company}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod 
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

# harry = Employee()
chris = Employee("Chris", 100, "Youtube")
prem = Employee("Prem", 300, "Facebook")
rahul = Employee("Rahul", 500, "Apple")
raj = Employee("Raj", 200, "Samsung")

rahul.getDetails() # by running this it is clear to us that constructor attached the details of rahul and not only of rahul but of all employees with them  