# Cookie Recipe Program
# Ask the user how many cookies they want to make
# Display the number of cups of each ingredient needed for the specified number
# of cookies

print ("To bake 100 cookies, you will require\n3 cups of sugar\n1.5 cups of butter\n4 cups of flour") 

#display question
num = input("How many cookies would you like to make? ")
print("You want to bake", num, "cookies")

#perform calculation
div = float(num)/100

sugar = div*3
butter = div*1.5
flour = div*4

print("Your recipe will require\n", sugar, "cups of sugar\n",butter, "cups of butter\n", flour, "cups of flour")