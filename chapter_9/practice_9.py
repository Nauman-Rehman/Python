import os # it is only installed for question 11

# # 1. WAP to read the text from a given file 'poem.txt' and find out whether it contains the word "twinkle"
# with open('poem.txt', 'w') as f:
#     f.write('''Twinkle twinkle little star
# how I wonder what you are
# up above the world so high 
# like a diamond in the sky''')

# with open('poem.txt') as f:
#    t = f.read()
#    print(t)
#    print(f.read()) # it don't write again because read function is already run before
#    if "twinkle" in t:
#        print("yes twinkle is present in the poem")
#    else:
#        print("yes twinkle is not present in the poem")


# # 2. The game() function in a program lets a user play a game and returns the score as an integer. 
# #    you need to read a file 'High_Score.txt' which is either blank or contains the previous High Score.
# #    you need to WAP to update the High Score whenever game() breaks the High Score   
# def game():
#     return 68

# score = game()
# with open("hiscore.txt") as f:
#     hiscore = f.read()
# if hiscore == '':
#     with open("hiscore.txt", 'w') as f:
#         f.write(str(score))
# elif (int(hiscore) < score): # it overwrites the score if new score is greater than the highest score by which new score is now highest
#     with open("hiscore.txt", 'w') as f:
#         f.write(str(score))


# # 3. WAP to generate multiplication tables from 2 to 20 and write it to the different files.
# #    Place these files in a folder for a 13-year old.
for i in range(2,21):
    with open(f"Tables/table_of_{str(i)}.txt",'w') as f: # here (Tables/) tell the compiler that put the files in Tables name folder 
        f.write(f"The table of {str(i)} is: \n\n")
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n") 


# # # 4. A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with # # # # by updating the same file 
# with open("donkey.txt",'w') as f:
#     f.write('''donkey is an animal,
# donkey is very smart animal,
# donkey works very hard for the owner of donkey,
# people mostly use donkey word for smart people''')
# # the above lines are not necessary if file is already exist we can start it from below    
# f = open("donkey.txt")
# content = f.read()
# content = content.replace('donkey', "##%&*@##")
# f.close()
# with open("donkey.txt", 'w') as f:
#     f.write(content)


# # 5. Repeat program 4 for a list of such words to be censored 
# words = ["donkey", "kaddu", "mote"]
# with open("donkey.txt") as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word,"##%&*#@@#")
# with open("donkey.txt",'w') as f:
#     f.write(content)


# # 6. Write a program to mine a log file and find out wheather it contains 'allocate'
# with open("log.txt") as f:
#     content = f.read()
# if "allocate" in content: # it is case sensitive so we can use [content.lower()] in place of content of only this line which makes all the characters of the file lower
#     print("yes it is present in the log")
# else:
#     print("no it is not present in the log")


# # 7. Write a program to find out the line number where allocate is present from ques 6 ******* (good question)
# content = True
# i = 1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if "allocate" in content:
#             print("\nyes it is present in the log\n")
#             print(f"at line number {i}")
#             print(content)
#             break
#         i+=1
#     else:
#         print("no it is not present in the log")

#     while content:
#         i+=1
#         content = f.readline()
#         if "allocate" in content:
#             print(f"at line number {i}")
#             print(content)


# # 8. Write a program to make a copy of a text file "this.txt"
# with open("copy_of_(this)_file.txt",'w') as f:
#     with open("this.txt") as f1:
#         content = f1.read()
#     f.write(content)


# # 9. write a program to find out whether a file is identical & matches the content of another file
# file1 = "this.txt"
# file2 = "copy_of_(this)_file.txt"
# with open(file1) as f1:
#     with open(file2) as f2:
#         if(f1.read() == f2.read()):
#             print("they both are same")
#         else:
#             print("they are different")


# # 10. Write a program to wipe out the contents of a file using python
# with open("blank.txt",'w') as f:
#     f.write('') # by writing this whatever be written in the file is overwrited by '' which is blank


# # 11. WAP to rename a file to "renamed_by_python.txt"
# oldname = "old.txt"
# newname = "renamed_by_python.txt"
# with open(oldname) as f:
#     content = f.read()
# with open(newname,"w") as f:
#     f.write(content)

# os.remove(oldname) # this function is use to delete a file