# # 1. Create a class programmer for storing information of few programmers working at microsoft
# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, gmail):
#         self.name = name
#         self.salary = salary
#         self.gmail = gmail
#     def getDetails(self):
#         print(f"The name of the employee is {self.name}")
#         print(f"His salary is {self.salary}")
#         print(f"His gmail-id is {self.gmail}")
# aman = Programmer("Aman", 50000, "aman@gmail.com")
# badal = Programmer("Badal", 40000, "badal@gmail.com")
# caterine = Programmer("Caterine", 45000, "caterine@gmail.com")
# daud = Programmer("Daud", 42000, "daud@gmail.com")
# aman.getDetails()
# badal.getDetails()
# caterine.getDetails()
# daud.getDetails()


# # 2. Write a class calculator capable of finding square, cube and squareroot of a number
# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"The square of {self.number} is {self.number **2}")
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number **3}")
#     def sqRoot(self):
#         print(f"The square root of {self.number} is {self.number **0.5}")
# a = Calculator(int(input("Enter the number: ")))
# a.square()
# a.cube()
# a.sqRoot()


# # 3. Create a class with a class attribute a ; create an object from it and set a directly using object.a = 0.
# # Does this change the class attribute ? The answer is no
# class alphabet:
#     a = "apple"
# object = alphabet()
# object2 = alphabet()
# print(object.a) # it prints apple
# print(object2.a)
# object.a = 0 # changing the object attribute
# print(object.a) # object attribute is changed
# print(object2.a) # it still printing apple so the class attribute is not change when we change an attribute of a particular object
# a = "banana"
# print(object.a) # it don't take a of previous line because it only takes the attributes not variables 
# # (so we come to a conclusion that the variables in class are known as attributes and the functions in class are known as methods)


# # 4. Add a static method in problem 2 to greet the user with hello
# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"The square of {self.number} is {self.number **2}")
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number **3}")
#     def sqRoot(self):
#         print(f"The square root of {self.number} is {self.number **0.5}")
#     @staticmethod    
#     def greet():
#         print('''\nWelcome to the world's best calculator platform.
# Here you will get the square, cube and the squre root a number.
# So......''')
# b = Calculator(1)
# b.greet()
# a = Calculator(int(input("Enter the number: ")))
# a.square()
# a.cube()
# a.sqRoot() 


# # 5. Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information of trains running under Indian Railways
# class Train:
#     tNumber = 00000
#     tName = ""
#     def setRoute(self,name,list,code):
#         self.name = name
#         self.route = list
#         self.code = code
# print("Welcome to New Delhi Railway Station")
# destination = input("Enter the destination: ")
# t1 = Train()
# l1 = ["Kochuveli","Surat","Vadodra","Kota","H Nizamuddin","New Delhi","Ambala Cant","Ludhiana","Jalandhar","Amritsar"]
# c1 = ["KVCL","ST","BRC","KOTA","NZM","NDLS","UMB","LDH","JUC","ASR"]
# t1.setRoute("Amritsar Express",l1,c1)
# if destination in t1.route or t1.code:
#     print("Available train",t1.name)
#     print(f'''Arrives from --> {t1.route[0]}
# via --> {t1.route[1:-2]} 
# and stops at --> {t1.route[-1]}''')


# # 5. Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information of trains running under Indian Railways
# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#     def getStatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {len(self.seats)}")
#     def fareInfo(self):
#         print(f"The price of the ticket is : {self.fare}")
#     def bookTicket(self):
#         if(len(self.seats) > 0):
#             print(f"Your ticket has been booked! Your seat number is {self.seats[0]}\n")
#             self.seats.remove(self.seats[0])
#         else:
#             print("Sorry this train is full! Kindly try in next time")
#     def cancelTicket(self):
#         a = input("Tell your seat number: ")
#         self.seats.insert(0,a)
#         print("Your seat is cancelled!")
# l1 = []
# for i in range(1,301):
#     l1.append(i)
# intercity = Train("Intercity Express: 14015", 90, l1)
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.cancelTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.cancelTicket()
# intercity.cancelTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.bookTicket()


# 6. Can you change the self parameter inside a class to sonething else (say 'harry'). Try changing 
class Sample:
    a = "Harry"
    def __init__(harry, name): # yes we can change self by other keyword
        harry.name = name
obj = Sample("Harry")
print(obj.name)