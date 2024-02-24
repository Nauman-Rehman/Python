
# this file is not made by me. This file comes into existance when we run a code by selecting some code of a file
# then first a file is automatically made and the selected code copied to this file and then the program is run for this file
# so this file is also come into existace by the upper procedure
class Employee:
    company = "Google"
    def getSalary(self): # what is the role of self here
        print(f"Salary is {self.salary}") # it prints the salary attribute of the object which is coming as self 
# so whatever be the instance is coming it prints the attribute defined in the program of that instance  
        print(f"Salary of the employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary() # this line is converted to another line when program is run and that line is written below
Employee.getSalary(harry) # so when 