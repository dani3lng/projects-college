#Creates Private class object

import enlistee

#create main def
def main():
    #get enlistee attribute information
    print('Please provide the following information.')
    name = input('Enter your full name: ')
    number = int(input('Enter your Enlistee number: '))

    #create enlistee object
    #enlist = enlistee.Enlistee(name, number)

    #get private attribute information
    platoon = int(input('Enter your Platoon number: '))
    service = int(input('Enter Year of Service: '))
    
    #create private object
    priv = enlistee.Private(name, number, platoon, service)

    #display date entered
    print('You have entered the following information.')
    print('-------------------------------------------')
    print('Full Name:', priv.get_name())
    print('Enlistee Number:', priv.get_number())
    print('Platoon Number:', priv.get_platoon())
    print('Years of Service:', priv.get_years())

#call main function
main()
    