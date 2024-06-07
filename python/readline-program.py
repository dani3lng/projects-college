#Line numbers program

#ask for file name
infile = open(input('Enter the name of a file: '), 'r')

#read lines
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()

#close file
infile.close()

#print data
print('Line 1:', line1)
print('Line 2:', line2)
print('Line 3:', line3)
