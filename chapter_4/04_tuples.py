# creating a tuple using ()
# we can't add, remove, or change a value in tuple it has immutable property
t = (1, 2, 3, 64)
t1 = () # this is my empty tuple
# t2 = (63 ) # wrong way to make a tuple. Without (,) it is only a number and not a tuple
t2 = (63, ) # this is a tuple with only one element here (,) is important to make it a tuple
print(t)
print(t1)
print(t2)

# the difference between list and tuple is that tuple can't be update we cannot update a tuple
# t[1] = 34 # this will show error because here we are trying to change the value of tuple

