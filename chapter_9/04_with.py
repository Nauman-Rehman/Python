# **************  with statement **************
# the best way to open and close the file automatically is the (with) statement
with open("this.txt", 'w') as f:
    f.write("file made and write by (with) statement")
# by the help of with statement we have no need to close file by f.close() as it is done automatically
