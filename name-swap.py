#Name Swap Program

#ask for first, middle, last
def main():
   #create list
    name_list = []

    #add names
    for names in range(1):
        #get users name
        first = input('Enter your first name: ')
        middle = input('Enter your middle name: ')
        last = input('Enter your last name: ')

        #append the name to list
        name_list.append(first)
        name_list.append(middle)
        name_list.append(last)

    #display full name
    print('Original name: ', name_list)

    #reverse list
    name_list.reverse()

    #display reversed name
    print('Reversed name: ', name_list)
    
        
#call main function
main()