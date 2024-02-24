a = 3
b = 4
print("The value of 3+4 is", a+b)
print("The value of 3+4 is", 3+4)
print(3+4) # this is go as an expression and the result or we can say that the output is not print as 3+4 but output is it's evaluation which is 7
print("The value of 3-4 is", a-b)
print("The value of 3*4 is", a*b)
print("The value of 3/4 is", a/b) # it prints 0.75 and not 0 like c++ 

# assignment operators
a += 7 # it adds 7 in the value of a 
print(a)
a += b*2 # it adds twice the value of b in the value of a
print(a,b)
a-= b # it subtracts value of b from the value of a 
print(a)
a-=7 # it subtracas 7 from the value of a
print(a)
a*=12 # it multiply value of a from 12
print(a)
a/=12 # it divide value of a from 12
print(a)

# comparison operators
b = (4>7) # now b becomes object of boolean class or a boolean operator which sees the expression written in brackets and print true or false according to the correctness of the expression
print(b) 
a+=b*2 # b is not more an integer so this statement is senseless and the value of a will remain same
print(a)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2)) # (and) operator only gives True when both bool1 and bool2 are True and in all other cases it gives False
print("The value of bool1 or bool2 is", (bool1 or bool2)) # (or) operator only gives False when both bool1 and bool2 are False and in all other cases it gives True
print("The value of not bool2 is", (not bool2)) # (not) operator gives True if input is False and vice versa