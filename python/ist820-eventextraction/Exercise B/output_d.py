### Exercise B Output D

print('Starting Output D')
# set file paths for logs
file_path1 = 'DataSource/LogA.strace'
# open the file LogA
file1=open(file_path1)
# read LogA content into memory object “lines” 
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
            print(f'The user provides the following keystrokes to the console: ')
            print(keystrokes)
      elif term3 in line and term2 in line:
            name_start = line.find('"')
            name_end = line.find('"', name_start + 1)
            message = line[name_start + 1 : name_end]      
            print(f"The console shows the following message to the user's eyes: ")
            print(message)