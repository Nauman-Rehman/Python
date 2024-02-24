def greet(name):
    print("Good day " + name)
    print("Good night", name)

def sum(num1, num2):
    return num1 + num2

def wish(name = "Stranger"): # this is default argument if there is no input in function calling then it take stranger as a default value of name
    print("Happy Birthday", name)

greet("nauman")
s = sum(6, 32)
print(s)
wish("nauman")
wish()