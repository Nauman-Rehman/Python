# # 1. WAP to create a dictionary of hindi words with values as there english translation provide user with an option to look it up
# dict = {"aasman": "sky",
#         "sardi": "winter",
#         "garmi": "summer",
#         "billi": "cat"}
# a = input("write a word in hindi to translate in english: ")
# print("the meaning of",a,"in english is",dict.get(a)) # this gives none if the input key is not in the dict
# print("the meaning of",a,"in english is",dict[a]) # this will give an error if the input key is not in the dict


# # 2. WAP to input eight numbers from the user and display all the unique numbers(once) 
# # so here we use set because set prints each number at once regardless that how many times it is present
# b = set()
# b.add(int(input("Write number 1: "))) 
# b.add(int(input("Write number 2: "))) 
# b.add(int(input("Write number 3: "))) 
# b.add(int(input("Write number 4: "))) 
# b.add(int(input("Write number 5: "))) 
# b.add(int(input("Write number 6: "))) 
# b.add(int(input("Write number 7: "))) 
# b.add(int(input("Write number 8: "))) 
# # by taking it as a integer it comes as integer and stay in set (b) in sorted order
# print("Unique numbers are",b)


# # 3. Can we have a set with 18(int) and '18'(str) as a values in it ?
# c = {1,3,56,3,"hello","byy","hii","byy",4.67,3.55,4.67}
# print(c)
# # yes we can store more than one type of value in the set and whatever be the type if the value comes more than once then it prints it only once
d = {18,"18"} # what if i put same value as a integer and as a string
print(d) # then it prints both because in it's point of 18 of int and "18" of str are different


# 4. What will be the length of following set S:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # here it gives length 2 and not 3 because it knows that 20, 20.0 are same values and it stores it once
print(s) # this prints --> {20, '20'} because it knows that 20 and 20.0 are same


# 5. What is the type of (e)
e ={}
print(type(e)) # if set is empty then it's type is dict not set


# # 6. Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names of friends are unique
# l1 = input("which is your favorite language: ")  
# l2 = input("which is your favorite language: ")  
# l3 = input("which is your favorite language: ")  
# l4 = input("which is your favorite language: ")  
# friendDict = {"Purabh": l1,
#               "Pachhim": l2,
#               "Uttar": l3,
#               "Dakshin": l4}
# print(friendDict)
# # 2nd method
# favLang = {}
# l1 = input("which is your favorite language Saurabh: ")  
# l2 = input("which is your favorite language Sumit: ")  
# l3 = input("which is your favorite language Shashank: ")  
# l4 = input("which is your favorite language Sohail: ")
# favLang['Saurabh'] = l1  
# favLang['Sumit'] = l2  
# favLang['Shashank'] = l3  
# favLang['Sohail'] = l4  
# print(favLang)


# # 7. If names of 2 friends are same, what will happen to the program of previous problem
# favLang2 = {}
# l1 = input("which is your favorite language Saurabh: ")  
# l2 = input("which is your favorite language Sumit: ")  
# l3 = input("which is your favorite language Saurabh: ")  
# l4 = input("which is your favorite language Sohail: ")
# favLang2['Saurabh'] = l1  
# favLang2['Sumit'] = l2  
# favLang2['Saurabh'] = l3  # so here the favourite languag of 1st saurabh is updated because dict takes unique keys
# favLang2['Sohail'] = l4  
# print(favLang2)


# 8. If languages of two friends are same, then what will happen to the program in problem number 6
# then there is no problem values can be identical but keys can't
favLang3 = {}
l1 = input("which is your favorite language Saurabh: ")  
l2 = input("which is your favorite language Sumit: ")  
l3 = input("which is your favorite language Shashank: ")  
l4 = input("which is your favorite language Sohail: ")
favLang3['Saurabh'] = l1  
favLang3['Sumit'] = l2  
favLang3['Shashank'] = l3  
favLang3['Sohail'] = l4  
print(favLang3)
