#coin toss program

import random

class Coin:
    def __init__(self):
        self.sideup = 'head'
    def toss(self):
        num = random.randint(0,1)
        if num == 0:
            self.sideup = 'head'
        else:
            self.sideup = 'tail'
    def getsideup(self):
        return self.sideup

coin = Coin()
headCount = 0
tailCount = 0
for i in range(20):
    face = coin.getsideup()
    print('Flipping coin...',face)
    if(face=='head'):
        headCount+=1
    else:
        tailCount+=1
    coin.toss()
print('Total number of head is: ' +str(headCount))
print('Total number of tail is: ' +str(tailCount))
