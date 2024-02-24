a = 2
# if(a>3):
#     print("The value of a is greater than 3")
# elif(a>13):
#     print("The value of a is greater than 7")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>17):
#     print("The value of a is greater than 7")
# else:
#     print("The value is not greater than 3 or 7")
# # here we can see that statement of (if) and all (elif) are correct but it executes only one statement which comes first
# # and if (if) statement gets true then it comes out from complete (if,elif,else) ladder 
# # and if (if) statement gets false then it go for further statements to check the satisfying statement

if(a>3):
    if(a<44):
        print("a is less than 44 and greater than 3")
    else:
        print("a is greater than 44")
else:
    print("a is less then 3")