# receive the price of each product
print ("Welcome")
num1 = input("What is the price of item 1? ")
num2 = input("What is the price of item 2? ")
num3 = input("What is the price of item 3? ")
num4 = input("What is the price of item 4? ")

# calculate the total price with sales tax at 9%
sum = float(num1) + float(num2) + float(num3) + float(num4)
print ("Your subtotal is %.2f" % sum)
print ("Sales tax is 9%")
tax = 0.09
taxed = tax * sum
print ("Sales tax added is %.2f" % taxed)
total = float(taxed) + float(sum)
print ("Your total is %.2f" % total)