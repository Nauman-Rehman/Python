class Remote():
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
# above 3 functions are methods of class (Player)

remote1 = Remote() # here we make an object named (remote1) of class (Remote())
player1 = Player() # here we make an object named (player1) of class (Player())

if(remote1.isLeftPressed()):
    player1.moveLeft()