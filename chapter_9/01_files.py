f = open('sample.txt', 'r')  # this open function opens the file sample.txt . Here writing ('r') is optional by default it open it in read mode
data = f.read() # this read function reads the entire text of file and store it in data
sub = f.read(5) # this reads only first 5 characters of file but here in above line we have already read the file so this not work (one file can be read at once)
print(data)
print(sub)
f.close() # this close function closes the file

s = open('sample2.txt')
text1 = s.read(10)
text2 = s.read(7)
text3 = s.read()
# the part which have read already can't be read again (see the output of below line)
print(text1)
print(text2)
print(text3)
s.close()

# there are 4 modes to open a file
# 1). r --> open for reading
# 2). w --> open for writing
# 3). a --> open for appenting (means to add changes)
# 4). + --> open for updating

# 'rb' will open for read in binary mode (use when we are working in binary file). Here (b) is necessary in 'rb'
# 'rt' will opne for read in text mode (use when we are working in txt file). Here (t) is not necessary in 'rt'
