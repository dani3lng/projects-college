#Daily Hours Program

week = 1
#set main function
def main():
    repeat()

#set repeat function
def repeat():
    for days in range (week):
        #get hours worked
        mon = float(input('Enter total number of hours worked for Monday: '))
        tue = float(input('Enter total number of hours worked for Tuesday: '))
        wed = float(input('Enter total number of hours worked for Wednesday: '))
        thr = float(input('Enter total number of hours worked for Thursday: '))
        fri = float(input('Enter total number of hours worked for Friday: '))
        hours = float(mon+tue+wed+thr+fri)
        print('Your total hours for this week are', hours)
        rpt = input('Are your hours correct? (y/n) ')
        if rpt == 'y':
            print('These are the hours you entered')
        else:
            repeat()
        #create a list
        hours_worked = [mon,tue,wed,thr,fri]
        #display hours worked
        for h in hours_worked:
            print(h)

#call main function
main()