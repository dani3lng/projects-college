### Exercise A

# log event counter for 'read' events
def counter_read(term):
    total = 0
    name = input('Name text file: ')
    for line in lines:
        if term in line:
            print(line, file=open(name, 'a'))
            total += 1
    print(f'Total number of events is {total}', file=open(name, 'a'))

# log event for 'read from keyboard' events
def log_key(term, term2):
    name = input('Name text file: ')
    for line in lines:
        if term in line and term2 in line:
            print(line, file=open(name, 'a'))

# log event for 'read from file' events
def log_file(term, term2, term3):
    name = input('Name text file: ')
    for line in lines:
        if term in line and term2 not in line and term3 not in line:
            print(line, file=open(name, 'a'))


## Output A
print('Starting Output A')
# output total number of 'read' events and each 'read' event
file_path = 'ist820-eventextraction/DataSource/LogA.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
counter_read(term)
# close the file 
file1.close()

## Output B
print('Starting Output B')
# output total number of 'read' events and each 'read' event
file_path = 'ist820-eventextraction/DataSource/LogB.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
counter_read(term)
# close the file 
file1.close()

## Output C
print('Starting Output C')
# output each 'read from keyboard' event
file_path = 'ist820-eventextraction/DataSource/LogA.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
term2='tty'
log_key(term, term2)
# close the file 
file1.close()

## Output D
print('Starting Output D')
# output each 'read from keyboard' event
file_path = 'ist820-eventextraction/DataSource/LogB.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
term2='tty'
log_key(term, term2)
# close the file 
file1.close()

## Output E
print('Starting Output E')
# output each 'read from keyboard' event
file_path = 'ist820-eventextraction/DataSource/LogA.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
term2='tty'
term3='pipe'
log_file(term, term2, term3)
# close the file 
file1.close()

## Output F
print('Starting Output F')
# output each 'read from keyboard' event
file_path = 'ist820-eventextraction/DataSource/LogB.strace'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# print read events to console
term=' read('
term2='tty'
term3='pipe'
log_file(term, term2, term3)
# close the file 
file1.close()

## Output G
print('Starting Output G')
# output a table for each log counting how many times a file was read
# create a list for file names and counts
file_names = []
counts = []
file_path = 'ist820-eventextraction/Outputs/ExerciseA-OutputE.txt'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
# find file names
file_name_start = lines.find('<')
file_name_end = lines.find('>')
file_name = lines[file_name_start + 1 : file_name_end]
# add file names to list
if file_name not in file_names:
		file_names.append(file_name)
print(file_names)
# create file counter
idx = file_names.index(file_name)
counts[idx] += 1
print(f'File Name    |    Counts')
for i in range(len(file_names)):
    print(file_name + '\n' + '\n' + counts)
# close the file 
file1.close()