# Cookie Recipe Program
# Ask the user how many cookies they want to make
# Display the number of cups of each ingredient needed for the specified number
# of cookies

print (f'''To bake 100 cookies, you will require:
       3 cups of sugar
       1.5 cups of butter
       4 cups of flour
       ''') 

#display question
num = input("How many cookies would you like to make? ")
print(f"You want to bake {num} cookies")

#perform calculation
div = float(num)/100

sugar = div*3
butter = div*1.5
flour = div*4

print(f'''
Your recipe will require:
      {sugar:.3f} cups of sugar 
      {butter:.3f} cups of butter 
      {flour:.3f} cups of flour
      ''')