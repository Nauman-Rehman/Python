class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    def changeSalary(self, sal):
        self.salary = sal # this only change the attribute of the instance
        self.__class__.salary = sal # this change the attribute of class, the alternative way to do this is defined in below method
    @classmethod # by use of classmethod we can directly access class attributes 
    def changeSalary(cls, sal): # taking cls (means class)
        cls.salary = sal # changing the attribute(salary) of class




        

e = Employee()
print(e.salary)
