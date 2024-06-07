def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 0.01
    else:
        res = 3 * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,3*(n-1), "): ",res)
        return res	

print(factorial(30))
total = 0
for x in range (30):
    value =float(input('Enter number: '))
    total = total + value
print(total)