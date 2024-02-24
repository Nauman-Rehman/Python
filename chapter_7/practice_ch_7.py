# # 1. WAP to print multiplicative table of a given number using for loop
# a = int(input("Enter the number table of which has to be written: "))
# print("The table of",a,"is :-")
# for i in range(1,11):
#     print(str(a),"x",str(i),"=",str(a*i))
#     # 2nd method to print
#     print(f"{a} x {i} = {a*i}") # in this method variable put in {} brackets and complete thing in f""


# # 2. WAP to greet all the person names stored in a list l1 and which starts with S
# l1 = ['aaftab','faizan','sohail','shadab','nauman','karim','sameer','siddarth']
# for name in l1:
#     if name.startswith('s'):
#         print("Welcome!", name)


# # 3. Attempt problem 1 with while loop
# a = int(input("Enter the number table of which has to be written: "))
# print("The table of",a,"is :-")
# i = 1
# while i<=10:
#     print(str(a),"x",str(i),"=",str(a*i))
#     i = i+1


# # 4. WAP to find wheather a given number is prime or not
# num = int(input("Enter the number: "))
# for i in range(2,num):
#     if (num%i == 0):
#         print("The number is not prime")
#         break
#     else:
#         continue
# else:
#     print("The number is prime")
    

# # 5. WAP to find the sum of first n natural numbers using while loop
# n = int(input("Enter a number: "))
# ans =0
# i = 1
# while i<=n:
#     ans = ans + i
#     i = i + 1
# print("The sum of numbers from 1 to",n,"is",ans)


# # 6. WAP to calculate the factorial of a given number using for loop
# a = int(input("Enter the number: "))
# ans = 1
# for i in range(1,a+1):
#     ans = ans*i
# print("Factorial of",a,"is",ans)


# # 7. WAP to print the following star pattern
# #      *
# #    * * *
# #  * * * * *

# # method 1
# n = int(input("Enter the number of lines: "))
# for i in range(n):
#     for j in range(2*(n - i+1)):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("* ", end="")
#     print("") 

# # method 2
# n = int(input("Enter the number of lines: "))
# for i in range(n):
#     print(" "*(2*(n-i+1)), "* "*(2*i + 1))


# # WAP to print following star pattern:
# #  *
# #  * *
# #  * * *

# # method 1
# n = int(input("Enter the number of lines: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print("")

# # method 2
# n = int(input("Enter the number of lines: "))
# for i in range(n):
#     print("* " * (i+1))

