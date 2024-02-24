class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self): # if i overwrite the same method then the instance of this class use this method rather then using the same named method of super(base) class
        print("This is a programmer")
        
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
