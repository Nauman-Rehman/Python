a = input("Enter your name ") # it takes input from user after write the inner sentence and that input value will become equal to the variable(a) 
# so that when we try to print (a) it prints that input value
print("Your name is",a)
# or we can write it
print(a)
# what is the type of vairable (a) by the way in this case ? let's check
print(type(a)) # it always take input in string type even if we give a numeric value in input
a = int (a) # here we have done typecasting but it converts when it is possible
print(type(a))