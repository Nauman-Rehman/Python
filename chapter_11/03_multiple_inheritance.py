class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.eCode)
print(p.company) # it gives the company of the class which is first inherit and here first inherit class is Freelancer
