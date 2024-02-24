# in the previous file we see that we need (self) when the attributes of different instances are different and we have to print them accordingly
# but what when we have to print the same thing for all objects or instances, let's take an example

class Employee:
    company = "Google"
    @staticmethod  # by writing it the upcoming call is come without any (self) character
# Difinition of @staticmetod --> Sometimes we need a function that doesn't use the self parameter we can define a static method
    def greet(): # this have no need of (self)
        print("Good morning") # this type of greeting is same for all

# we can also give some more things with self while calling
    def name(self, country, age):
        print(f"Our employee is born in {country} and he is {age} years old")
        

harry = Employee()
harry.greet() # this through me an error because it converts in --> Employee.greet(harry)
# which is showing that harry is going as self but the recieving function(greet) don't takes self 
# so in order to overcome with this type of problem we write --> (@staticmethod) before defining the function
# by writing it, [harry.greet()] is converted to [Employee.greet()] and not in [Employee.greet(harry)]
# so, the problem is solved
harry.name("India", "25")



