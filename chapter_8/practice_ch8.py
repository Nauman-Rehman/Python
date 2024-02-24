# 1. WAP using function to find greatest of three numbers
def greatest(a,b,c):
    if(a>b):
        big = a
    else:
        big = b
    if(big > c):
        print("Greatest among these three numbers is", big)
    else:
        print("Greatest among these three numbers is", c)

a,b,c = map(int,input("Enter three numbers: ").split()) # this map and split is used in this form to get more than 1 input at a time
greatest(a,b,c)


# 2. WAP using function to convert Celsius to Fahrenhiet
def change_scale(celcius):
    return (celcius*9/5) + 32
temp = int(input("Enter the temparature in Celsius: "))
print("The temparature",temp, "in Fahrenhiet scale is",change_scale(temp))


# 3/ How do you pravent a python print() function to print a new line at the end
# by writing and funtion
print("Write next line in this line. ", end="")
print("I have write a new line in same line")


# 4. Write a recursive function to calculate the sum of first n natural numbers
def sum_n(n):
    if(n==0):
        return 0
    sum = n + sum_n(n-1)
    return sum

n = int(input("Enter a number: "))
print("The sum of numbers from 1 to",n,"is =",sum_n(n))


# 5. WAP to print first n lines of the following pattern
#  * * *
#  * *
#  *
def pattern(n):
    for i in range(n):
        print("* "*(n-i))
n = int(input("Enter the number of lines: "))
pattern(n)



# 6. Write a python function to remove a given word from a string and strip it at the same time
def remove_and_strip(string, word):
    newStr = string.replace(word, "") # it replaces input word from blank
    return newStr.strip() # it strips means remove extra spaces from start and from end

this = "     Harry is a good boy     "
n = remove_and_strip(this, "Harry")
print(n)