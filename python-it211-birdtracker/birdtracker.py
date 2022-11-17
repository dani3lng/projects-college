#4 days

total = 0
day = 0
keep = 'y'

print('Bird Watching Tracker')
print('---------------------')
while keep == 'y':
    days = int(input('What day is it? '))
    length = (day + days)
    bird = int(input('How many birds have you see today? '))
    total = total + bird
    print('Total number of birds seen today is', total)
    keep = input('Do you want to continue? (y/n) ')
    

avg = total/length
print('The average number of birds per day is %.0f' % avg)