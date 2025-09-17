### Exercise B Output E

# name variable for text file
name = input('Name text file: ')

print('Starting Output E')
# set file paths for logs
file_path1 = 'DataSource/LogB.strace'
# open the file LogB
file1=open(file_path1)
# read LogB content into memory object “lines” 
lines=file1.readlines()
# close the file 
file1.close()

# find read, keyboard LogB events
term1=' read('
term2='tty'
term3=' write('
for line in lines:
      if term1 in line and term2 in line:
            name_start = line.find('"')
            name_end = line.find('"', name_start + 1)
            keystrokes = line[name_start + 1 : name_end]
            print(f'The user provides the following keystrokes to the console: ', file=open(name, 'a'))
            print(keystrokes, file=open(name, 'a'))
      elif term3 in line and term2 in line:
            name_start = line.find('"')
            name_end = line.find('"', name_start + 1)
            message = line[name_start + 1 : name_end]      
            print(f"The console shows the following message to the user's eyes: ", file=open(name, 'a'))
            print(message, file=open(name, 'a'))
