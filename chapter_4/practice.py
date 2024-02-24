# # write a program to store seven fruits in a list entered by a user
# f1 = input("Enter Fruit number 1 ")
# f2 = input("Enter Fruit number 2 ")
# f3 = input("Enter Fruit number 3 ")
# f4 = input("Enter Fruit number 4 ")
# f5 = input("Enter Fruit number 5 ")
# f6 = input("Enter Fruit number 6 ")
# f7 = input("Enter Fruit number 7 ")
# myFruitList = [f1, f2, f3, f4, f5, f6, f7]
# print(myFruitList)


# # write a program to accept marks of 6 students and display them in a sorted manner
# s1 = int (input("Enter the marks of student s1: "))
# s2 = int (input("Enter the marks of student s2: "))
# s3 = int (input("Enter the marks of student s3: "))
# s4 = int (input("Enter the marks of student s4: "))
# s5 = int (input("Enter the marks of student s5: "))
# s6 = int (input("Enter the marks of student s6: "))
# # all the input values are taken in int form because initially input is always in the form of string
# marksOfStudents = [s1, s2, s3, s4, s5, s6]
# print(marksOfStudents)
# # print(marksOfStudents.sort()) # this gives none output 
# marksOfStudents.sort()
# print(marksOfStudents)


# write a program to sum a list with 4 numbers
l = [3,56,3,6]
print(l[0] + l[1] + l[2] + l[3]) 
print(sum(l)) # this sum function gives the some of all the values of l


# write a program to count the number of zeros in the following tuple
a = (7,0,8,0,0,9)
print(a.count(0))