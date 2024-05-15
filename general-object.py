#This program creates a General obejct

import enlistee

#main defintion
def main():
    #ask for information
    print('Provide the following information.')
    print('----------------------------------')
    name = input('Full name: ')
    number =int(input('Enlistee Number: '))
    salary = float(input('Annual Salary: '))
    bonus = float(input('Annual Bonus: '))

    #create general object
    general = enlistee.General(name,number,salary,bonus)

    #display data entered
    print('You have entered the following information.')
    print('-------------------------------------------')
    print('Full Name:', general.get_name())
    print('Enlistee Number:', general.get_number())
    print('Annual Salary:', general.get_salary())
    print('Annual Bonus:', general.get_bonus())

#call main function
main()