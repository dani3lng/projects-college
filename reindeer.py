#This program displays corresponding name of Santa's reindeer
#1 = Dasher, 2 = Dancer, 3 = Prancer, 4 = Vixen, 5 = Comet, 6 = Cupid
#7 = Donner, 8 = Blitzen


#main function
def main():
    #display message
    print("Welcome")
    #message function
    message()
    
#message function
def message():
    #request number
    num = input("Enter a number between 1 through 8. ") 
    if num == "1":
        print("Number 1 is Dasher")
    if num == "2":
        print("Number 2 is Dancer")
    if num == "3":
        print("Number 2 is Prancer")
    if num == "4":
        print("Number 2 is Vixen")
    if num == "5":
        print("Number 2 is Comet")
    if num == "6":
        print("Number 2 is Cupid")
    if num == "7":
        print("Number 2 is Donner")
    if num == "8":
        print("Number 2 is Blitzen")
    if num < "1" or num > "8":
        print("Invalid number.")
    #ask to continue
    keep_going = input("Would you like to choose another numer? (y/n) ")
    #create if statement
    if keep_going == "y": 
        message()
    if keep_going == "n":
        print("Thank you\nHave a nice day!")


#call main function
main()