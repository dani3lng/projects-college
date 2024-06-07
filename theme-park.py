#Program shows admission discount
#2 or less - free admission
#Older than 2, less than 14 - pays half price
#14 to less than 55 - pays full price
#55 or greater - pays half price

#main function
def main():
    #welcome
    print("Welcome to the theme park.")
    #call year function
    year()

#year function
def year():
    #ask for age
    age = input("Please enter your age. ")
    if age<='2':
        print("Congrats, you get free admission!")
        
    if age>'2' and age<'14':
        print("Congrats, you get half price tickets!")
        
    if age>='55':
        print("Congrats, you get half price tickets!")

    if age>='14' and age<'55':
        print("Your tickets will be at full price.")
        
    #repeat
    repeat = input("Do you have additional people? (y/n) ")
    if repeat == "y":
        year()
    if repeat == "n":
        #print message
        print("Have a great time!")
        
#call main function
main()
