# wish = "Good Morning, "
# name = input("Please tell me your name:\n ")
# print(wish + name)


# input("Dear ")
# print("\t You are Selected!")
# input("Date:- ")

# when we have to send same email or letter to many people with mentioned their name and different dates
letter = '''Dear,  (name)
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date:- (date)'''
name = input("Enter the name: ")
date = input("Enter the date: ")
letter = letter.replace("(name)", name)
letter = letter.replace("(date)", date)
print(letter)
print(letter.find("  ")) # it finds out double spaces in the string
letter = letter.replace("  "," ") # it replace double space with single space 
# the above function replace every double space with single space. if there are two souble spaces together then it convert both in single but because they were together a new double space comes from 4 spaces to 2
print(letter)