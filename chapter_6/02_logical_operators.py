# (&&) = and, (||) = or, (!=) = not

age = int(input("Enter your age: "))
# if(age>34 and age<56):
#     print("You can work with us")
# else:
#     print("You can't work with us") 

if(age<34 or age>56):
    print("You can't work with us")
else:
    print("You can work with us") 