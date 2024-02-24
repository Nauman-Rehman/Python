for i in range(10):
    print(i)
    if i == 5:
        break # it makes the program to come out from loop
else: # it only runs when loop is successfully run completely but in above line we can see that loop is breaked in between so this else don't work
# note the (else) written above is not the (else) of (if), it is the (else) of (for loop)  
    print("loop is successfully completed")
# if i write the above (print) line without else statement then the (print) line prints regardless of loop is successfully complete or not