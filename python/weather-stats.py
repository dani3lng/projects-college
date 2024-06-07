#Weather Statistics Program
#DAY constant holds the number of days for weekly temp

DAY = 7

def main():
    #create list to hold the temp of each day
    temp = [0] * DAY

    #create a variable to use as an accumulator
    total = 0

    #create variable to hold an index
    index = 0

    print('Enter the temperature for each day: ')

    #get the temperature for each day
    for index in range (DAY):
        print('Day #', index + 1, ':', sep='', end='')
        temp[index] =int(input())
        index += 1

    #display the values entered
    print('Here are the following values.')
    print(temp)

    #calculate total
    for value in temp:
        total += value
        avg_temp = total / DAY

    #display avg
    print('The average temperature for this week is %.0f' % avg_temp)

    #display min and max
    print('The lowest temperature is', min(temp),'F')
    print('The highest temperature is', max(temp),'F')

#call main function
main()