a = {2,16,8,7,6,9,0,100,93,68}
b = set()
b.add(4) # adding an item in set b
b.add(5) # adding an item in set b
b.add(6)
b.add(8)
b.add(7)
b.add(9)

# b.add(6,7,8,9) # can't add more than one item in a set at a time 
print(b)

b.add((5,7,3,5,94,1)) # can we add a tuple in a set
# if there is same element in the set and in the tuple we are adding in the set then set take them both and one element can come more than one time in a tuple
print(b) # yes we can add a tuple in a set
b.add(54)
b.add(88)
print("the value of b is",b)
 
print("the value of a union b is",a.union(b)) # it prints the union of a and b
print("the value of a intersection b is ",a.intersection(b)) # it prints the intersection of a and b
print("the value of a - b is",a - b)


# b.add([57,74,875,4,2,3]) # can we add a list in the set
# print(b) # showing error so we can't add a list in a set

# b.add({4:5}) # can we add dictionary in a set 
# print(b) # the answer is no

# so can't add list and dictionary in set , but can add a tuple in the set
# ********* the actual thing is that the thing which is mutable or can be change in future can't be add in set but the thing which is immutable or can't be change, can be add in set


# some points to be noted
# sets are unodered (can't access by index)
# there is no way to change items in sets but we have seen that we can add items in it
print(len(b))
# b.remove(94) # this shows an error because 94 is not only present in set (b) but also in the tuple
b.remove(4)
print(b)

print(b.pop())
print(b)
print(b.pop())
print(b)
print(b.pop())
print(b)
# i am seeing that it is using LIFO process but i am not sure that it always pop with LIFO process

# b.clear() # this command completely clear the set
