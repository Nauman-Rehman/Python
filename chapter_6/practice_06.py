# # WAP to find greatest of four numbers entered by the user
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# d = int(input("Enter number 4: "))

# if(a>b):
#     f1 = a
# else:
#     f1 = b
# if(c>d):
#     f2 = c
# else:
#     f2 = d
# if(f1 > f2):
#     ans = f1
# else:
#     ans = f2
# print("The greatest of all number is",ans )


# # WAP a program to find out whether a student is pass or fail, if it requires total of 40% and at least 33% in each subject to pass
# # Assume 3 subjects and take marks as an input from the user
# sub1 = int(input("Enter marks of first subject: ")) 
# sub2 = int(input("Enter marks of second subject: ")) 
# sub3 = int(input("Enter marks of third subject: ")) 
# total = (sub1 + sub2 + sub3)/3
# if(sub1<33 or sub2<33 or sub3<33 or total<40):
#     print("you are fail")
# else:
#     print('''Congrats!
#           you have passed.''')


# # A spam comment is defined as a text containing following keywords
# # "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams
# comment = input("Comment here: \n")
# if("make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment ):
#     print ("It is a spam")
# else:
#     print("This messege is not a spam")


# # 4. WAP to find whether a given username contains less than 10 character or not
# username = input("Write a username with atleast 10 characters: \n")
# if(len(username)<10):
#     print("Username is too small, please enter username with at least 10 characters")
# else:
#     print("Your username is", username)


# # WAP which finds out whether a given name is present in a list or not
# list = ["sohail", "gaurav", "uday", "lalit", "faizan", "vishal"]
# name = input("Enter your name: \n")
# if(name in list):
#     print("Yes! your name is present in the list")
# else:
#     print("Sorry! Your name is not mentioned in the list")
# # but here it is case sensitive
    

# WAP to calculate the grade of a student from his marks from the following scheme
# 90 - 100 = Ex
# 80 - 90 = A
# 70 - 80 = B
# 60 - 70 = C
# 50 - 60 = D
# < 50 = F
# marks = int(input("Enter your marks to get your grade: "))
# # method 1
# if(90 < marks and marks <= 100):
#     grade = "Ex"
# elif(80 < marks and marks <= 90):
#     grade = "A"
# elif(70 < marks and marks <= 80):
#     grade = "B"
# elif(60 < marks and marks <= 70):
#     grade = "C"
# elif(50 < marks and marks <= 60):
#     grade = "D"
# elif(0 <= marks and marks <= 50):
#     grade = "F"
# if(grade == "F"):
#     print("You are fail")
# else:
#     print("Your grade is",grade)

# # method 2
# if(90 < marks):
#     grade = "Ex"
# elif(80 < marks):
#     grade = "A"
# elif(70 < marks):
#     grade = "B"
# elif(60 < marks):
#     grade = "C"
# elif(50 < marks):
#     grade = "D"
# elif(0 <= marks):
#     grade = "F"
# if(grade == "F"):
#     print("You are fail")
# else:
#     print("Your grade is",grade)


# 7. WAP to find out whether a post is talking about "Harry" or not
post = input("Write a post\n")
if("harry" in post):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")