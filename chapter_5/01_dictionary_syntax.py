myDict = {
    "Fast": "In a Quick Manner",
    "Nauman": "Learning coding",
    "Marks": [1,2,5],
    'Fast': "Cheetah is fast", # if we make a key with duplicate name then it get overwrite means old value of fast is not more and now fast has this new value
    "anotherDict": {"Nauman": "noobPlayer"}  # nested dictionary
}

print(myDict['Fast'],myDict['Nauman'],myDict['Marks'])
print(myDict['Fast'])
print(myDict['Nauman'])
print(myDict['Marks'])
myDict['Marks'] = [67,34,75] # dictionary is mutable means can be changed
print(myDict['Marks'])
print(myDict['anotherDict'])
print(myDict["anotherDict"]['Nauman']) # print the value of that nauman who(which) is the value of anotherDict
a = input("enter the number: ")
print(a)