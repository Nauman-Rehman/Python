class Employee:
    company = "Google"

harry = Employee()
rajni = Employee()
print(harry.company) # it prints the company name Google
print(rajni.company) # it prints the company name Google

Employee.company = "Youtube" # company name of class (Employee) is changed
print(harry.company) # it prints the company name Youtube because the company name is changed 
print(rajni.company) # it prints the company name Youtube because the company name is changed

harry.company = "Facebook" # here attribute(company) of only instance(object or harry) is changed
print(harry.company) # it prints the company name of harry as (Facebook)
print(rajni.company) # it prints the company name of rajni as (Youtube) as changed earlier

# so here we have understand that instance attributes take preference over class attributes during assignment and retrival
# means when change the attribute of object outside the class, then the attribute define in the class is no longer considered for that object
 