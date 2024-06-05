#This program creates a Person object

import person_class

#main definition
def main():
    
    #get information
    print('Provide the following information')
    print('---------------------------------')
    first = input('First Name: ')
    last = input('Last Name: ')
    number = int(input('Telephone Number: '))
    customer = int(input('Customer Number: '))
    call = input('Would you like to be on our call list (y/n)? ')

    #create person object
    custmer = person_class.Customer(first,last,number,customer,call)

    #display data entered
    print('The following information has been entered.')
    print('-------------------------------------------')
    print('First Name:', custmer.get_first())
    print('Last Name:', custmer.get_last())
    if call == 'y':
        print('Telephone Number:', custmer.get_number())
    else:
        print('Customer declined to be on the call list.')
    print('Customer Number:', custmer.get_customer_number())

#call main
main()
