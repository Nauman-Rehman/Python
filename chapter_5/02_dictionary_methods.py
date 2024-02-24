myDict = {
    "fast": "In a Quick Manner",
    "nauman": "Learning coding",
    "marks": [1,2,5],
    'fast': "Cheetah is fast", # if we make a key with duplicate name then it get overwrite means old value of fast is not more and now fast has this new value
    "anotherDict": {"nauman": "noobPlayer"},  # nested dictionary
    2:364  # here also 2 declared as a key and 364 as it's value
}
# dictionary methods
print(myDict.keys()) # it write the names of keys and if there is a key coming 2 times then write it only at once when it comes first time
print(type(myDict.keys())) # it gives the type of this dictionary keys 
print(list(myDict.keys())) # it write it in the type of list
print(type(myDict.keys())) # type remains same as dict_keys
print(myDict.values()) # it prints the values of the keys of myDict
print(type(myDict.values())) # the type of this is dict_values
print(myDict.items()) # it gives keys with their values means it gives keys and values both

addItem = { "Lovish": "Friend"} # making a new item with key Lovish and value Friend
addItems = {"divya": "friend",
            "shubham": "friend",
            "nitin": "friend"}
myDict.update(addItem) # adding this new item into (myDict) dictionary
print(myDict)
myDict.update(addItems) # it adds multiple item at a time because there are multiple items in (addItems)
print(myDict)

# there are 2 ways to get the value of a key
print(myDict.get("nauman")) # this line gives the value of nauman
print(myDict["nauman"]) # this line is also gives the value of nauman
# then what is the difference lets understand
# what if i want a value of a key which is not present in the dictionary
print(myDict.get("nauman2")) # this line gives (none) in output
print(myDict["nauman2"]) # but this line gives an error because in this way availability of key is necessary in the dictionary
