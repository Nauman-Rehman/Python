# list

a = [1,2,4534,45,67,4]
b = (1,2,4534,45,67,4) # if we write it in () this brackets then this is not more a list and became tuple which we study further
 
# print[a] # this shows error because print function don't use [] this kind of brackets
print(a)
print(a[3]) # this don't show an error
# print(a[0,3])  # this will show an error
a[3] = 789  # this has changed the value of 3rd index
print(a)
print(b)

# we can also create a list with items of different type
c = [45, "nauman", False, 3,9, 'D']
print(c)

