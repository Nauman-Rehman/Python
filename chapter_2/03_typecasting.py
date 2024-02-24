# typecasting is a method to change the datatype of any variable. It just try to change the datatype not sure that it will do it
# for example
a = "345"  # here a is a string because the number is written in double quotes
# print(a + 5) # it gives me an error because I am trying to add an integer in an string
# so what would i have to do ?
# I have to do typecasting 
a = int(a) # i have change the datatype of variable a from string to int
print (a + 5) # now it will add up 5 in 345
# Why I said that it will only try to change the datatype and not sure that it will able to change it ?
# Beause what will happen if i make a string variable
b ="Nauman" # in this case typecasting can't convert b from string to int 

# str(31) changes 31 to "31" => Integer to string conversion
# int("32") changes "32" to 32 => string to integer conversion
# float(32) cahnges 32 to 32.0 => integer to float conversion 
