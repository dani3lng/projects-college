#Write lines of code

def main():
    #open a file named test.txt
    outfile = open('test.txt', 'w')

    #write the lines of text
    outfile.write('This is a test for M3A1 Lab for IT211-1.')
    outfile.write('This is a test for M3A1 Lab for IT211-2.')
    outfile.write('This is a test for M3A1 Lab for IT211-3.')
    outfile.write('This is a test for M3A1 Lab for IT211-4.')

    #close the file
    outfile.close()

#call main function
main()