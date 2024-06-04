#$1 per day increase
#ask initial pay
#make table

add = 0

#beginnging
pay_initial = float(input('What is your current salary? '))
print('You entered $', (format(pay_initial, ',.2f')))

day = int(input('Enter requested number of days: '))
for number in range(1, day):
    num = number + 1
    print('Day\t Dollar Increase')
    print('-----------------------')
    print(number, '\t', num)

print('Your total increase for the period of', day, 'days is $', num)
print('Your final value is $', num + pay_initial)
