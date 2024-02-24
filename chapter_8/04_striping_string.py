this = "      Once    upon  a time there is a        cow     "
print(this) # this write in the same way as written above with extra spaces
print(this.strip()) # this also write in the same way but only delete extra spaces from start and end but not from mid

# Ques). Write a python function to remove a given word from a string and strip it at the same time
def remove_and_strip(string, word):
    newStr = string.replace(word, "") # it replaces input word from blank
    return newStr.strip() # it strips means remove extra spaces from start and from end

this = "     Harry is a good boy     "
n = remove_and_strip(this, "Harry")
print(n)