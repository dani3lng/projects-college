#Date Printer Program

#define main function
def main():

    #create string with a date
    date_string = input('Enter the date (mm/dd/yy): ')

    #split the date
    date_list = date_string.split('/')

    #display each piece of the date
    if int(date_list[0]) == 1:
        date_list[0] = 'January'
    elif int(date_list[0]) == 2:
        date_list[0] = 'February'
    elif int(date_list[0]) == 3:
        date_list[0] = 'March'
    elif int(date_list[0]) == 4:
        date_list[0] = 'April'
    elif int(date_list[0]) == 5:
        date_list[0] = 'May'
    elif int(date_list[0]) == 6:
        date_list[0] = 'June'
    elif int(date_list[0]) == 7:
        date_list[0] = 'July'
    elif int(date_list[0]) == 8:
        date_list[0] = 'August'
    elif int(date_list[0]) == 9:
        date_list[0] = 'September'
    elif int(date_list[0]) == 10:
        date_list[0] = 'October'
    elif int(date_list[0]) == 11:
        date_list[0] = 'November'
    elif int(date_list[0]) == 12:
        date_list[0] = 'December'
    print('Month:',date_list[0])
        
    print('Day:', date_list[1])
    
    if int(date_list[2]) > 30:
        year19 ='19'
        year19 += (date_list[2])
        print('Year:',year19)
    else:
        year20 = '20'
        year20 += (date_list[2])
        print('Year:',year20)

#call main function
main()
