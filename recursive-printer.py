#Recursive printing
    
def message(n):
    if n > 0:
        print(n)
        message(n-1)

n = int(input('Enter an integer: '))
message(n)
