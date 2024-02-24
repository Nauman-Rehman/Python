f = open("sample.txt")
data = f.readline() # readline function read only 1 line
print(data)
data = f.readline() # and again it call the next line but not more than 1 line
print(data)
f.close()

