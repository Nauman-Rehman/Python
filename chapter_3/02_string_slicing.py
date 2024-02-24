name = "nauman "
surname = "rehman"
print(name + surname) # it prints full name known as concatenating two strings
print(type(name))
print(name[0],name[2],name[4]) # it gives me the character of that index of name
# name[3] = "d" # --> we can't change character of any index of string. It doesn't work
print(name[1:4]) # it prints the character from 1 to 3(1 less than the value written after (:) but start from the value written before(:))
# the above line is also written as
print(name[:4]) # in this it automatically consider 0 before (:)
print(name[2:]) # in this it automatically consider the length of string after (:) and prints complete name start from 2nd index and end with last character
# when we don't know the size of string and want to print some last part of the string then we use negative counting in which (-1) represents the last character and (-2) represents second last ans so on
print(name[-4:-1]) # it prints the name from last character to third last 
print (name[-2:-5])# :: note --> we can't print name or part of name or string in reverse order by using this

fullname = "NaumanRehmanMansoori"
print(fullname[0:17:2]) # it prints characters from 0th index to 16th index and skip every 2nd index character  
