#Rock-Paper-Scissors program
#paper>rock
#rock>scissors
#scissors>paper

def main():
    print("Welcome to Rock, Paper, and Scissors")
    chal()
    
def chal():

    item1 = input("Choose your first item. ")
    if item1 == 'paper':
        item1 = 'paper'
    elif item1 == 'rock':
        item1 = 'rock'
    elif item1 == 'scissors':
        item1 = 'scissors'
    else:
        print('Invalid input')

    item2 = input("Choose your second item. ")
    if item2 == 'paper':
        item2 = 'paper'
    elif item2 == 'rock':
        item2 = 'rock'
    elif item2 == 'scissors':
        item2 = 'scissors'
    else:
        print('Invalid input')

    print('You chose', item1, 'vs', item2,)
    if item1 =='paper' and item2 =='rock':
        print('Paper Wins! Because paper wraps around the rock')
    if item1 =='paper' and item2 =='scissors':
        print('Scissors Wins! Because scissors cuts paper')
    if item1 =='paper' and item2 =='paper':
        print('Tie')

    if item1 =='rock' and item2=='rock':
        print('Tie')
    if item1=='rock' and item2=='paper':
        print('Paper Wins! Because paper wraps around the rock')
    if item1=='rock' and item2=='scissors':
        print('Rock Wins! Because rock breaks scissors')

    if item1=='scissors' and item2=='rock':
        print('Rock Wins! Because rock breaks scissors')
    if item1=='scissors' and item2=='paper':
        print('Scissors Wins! Because scissors cuts paper')
    if item1=='scissors' and item2=='scissors':
        print('Tie')

    cycle = input('Would you like to play again? (y/n) ')
    if cycle == 'y':
        chal()
    if cycle == 'n':
        print('Thanks for playing')

main()