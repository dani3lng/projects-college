#Random Number program

import random

number = open("random number.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 5))
    number.write(line)
    print(line)

number.close() 
