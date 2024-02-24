f = open('another.txt', 'w') # when we open in 'w'(write mode), it is not compulsory that file should be exist before. 
# if file is not exist and we are try to open it in 'w'(write mode) then this mode first make the file and then opne it in 'w' mode
# but this not works in 'r' mode 
f.write("Please write this to the file") # so we make a txt file and had write this sentence in it
f.close()

# what if I again open it in 'w' mode and write a new line
f = open('another.txt', 'w')
f.write("This is a new line try to add in this file . I think it delete's all the existed texts written before in this file ")
f.close()
# it delete's all the existed text written before in this file
# then what to do to add a new line

# to add a new line open it in appending 'a' mode
f = open('another.txt', 'a')
f.write('\nthis is a new line adding in this file in appending mode and this will not delete the previous existed texts')
f.close()
# whenever be opened in append mode it continues adding new things from existed file
# but write mode delete all the existed texts from the file and make it new

# but if we write by write function in write mode again and again then it writes every time for example
f = open('sample2.txt', 'w')
f.write("apple is a fruit")
f.write("\nbanana is also a fruit")
f.write("\nmango is also a fruit")
f.write("\npapaya is also a fruit")
f.write("\nkiwi is also a fruit")
f.close()
