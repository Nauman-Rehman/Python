import random

# snake, water, gun game or stone, paper, scissor game
def You_Win(comp, you):
    if comp == you:
        return None
    elif comp == "Snake":
        if you == "Water":
            return False
        else:
            return True
    elif comp == "Water":
        if you == "Gun":
            return False
        else:
            return True
    elif comp == "Gun":
        if you == "Snake":
            return False
        else:
            return True

print ("Comp Turn: Snake, Water, Gun ?")
randNo = random.randint(1,3) # (random.randint()) is a function use to generate a random number in a range given in brackets, [here 1 to 3]
if randNo == 1:
    comp = "Snake"
elif randNo == 2:
    comp = "Water"
elif randNo == 3:
    comp = "Gun"

you = input("Your Turn: Snake, Water, Gun ? ")


if you == "s":
    you = "Snake"
elif you == "w":
    you = "Water"
elif you == "g":
    you = "Gun"

Win_or_not = You_Win(comp,you)

print("Comp chose -->", comp)
print("You chose -->", you)

if Win_or_not == None:
    print("Match Tie!")
elif Win_or_not == True:
    print("You Win!")
else:
    print("You lose!")