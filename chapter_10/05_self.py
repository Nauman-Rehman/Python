class Employee:
    company = "Google"
    def getSalary(self): # what is the role of self here
        print(f"Salary is {self.salary}") # it prints the salary attribute of the object which is coming as self 
# so whatever be the instance is coming it prints the attribute defined in the program of that instance  
        print(f"Salary of the employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary() # this line is converted to another line when program is run and that line is written below
Employee.getSalary(harry) # so when the above line is converted to this line then what is happening here
#  it is just like calling a function of class with input (harry)
# but if the function [getSalary()] is defined as taking nothing in input by removing (self) from it's brackets
# and we are sending harry as input then there is something like contradictions because of which program through an error
# the error is --> Employee.getSalary() takes 0 positional arguments but 1 was given
# which means that the method [getSalary()] taked 0 arguments means nothing
# and 1 was given means the (harry) given while calling