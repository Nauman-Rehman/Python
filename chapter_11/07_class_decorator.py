class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 500
    # totalSalary = 6100 # but wait! what if i change the bonus or salary it would affect totalSalary so when i change any one above them i also have to change this one
    # so in order to overcome with this problem 
    @property
    def totalSalary(self): # this is not a method or function because it don't directly work for an object but behave as a property
        return self.salary + self.salarybonus
    # and this thing is known as getter

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)  
e.totalSalary = 5800 # changing the total salary, so we have to make a setter --> totalSalary.setter (to set the bonus)
print(e.salary)
print(e.salarybonus) # it prints the bonus 200 not 500 because because when we set totalSalary = 5800 and change the bonus in setter then bonus decreased by 300
