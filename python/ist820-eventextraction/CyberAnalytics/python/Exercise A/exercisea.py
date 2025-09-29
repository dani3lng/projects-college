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
user_input = input('Would you like to perform Output A: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output total number of 'read' events and each 'read' event
    file_path = 'DataSource/LogA.strace'
    # open the file
    file1=open(file_path)
    # read content into memory object “lines” 
    lines=file1.readlines()
    # print read events to console
    term=' read('
    counter_read(term)
    # close the file 
    file1.close()
else:
    pass

## Output B
print('Starting Output B')
user_input = input('Would you like to perform Output B: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output total number of 'read' events and each 'read' event
    file_path = 'DataSource/LogB.strace'
    # open the file
    file1=open(file_path)
    # read content into memory object “lines” 
    lines=file1.readlines()
    # print read events to console
    term=' read('
    counter_read(term)
    # close the file 
    file1.close()
else:
    pass

## Output C
print('Starting Output C')
user_input = input('Would you like to perform Output C: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output each 'read from keyboard' event
    file_path = 'DataSource/LogA.strace'
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
else:
    pass

## Output D
print('Starting Output D')
user_input = input('Would you like to perform Output D: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output each 'read from keyboard' event
    file_path = 'DataSource/LogB.strace'
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
else:
    pass

## Output E
print('Starting Output E')
user_input = input('Would you like to perform Output E: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output each 'read from keyboard' event
    file_path = 'DataSource/LogA.strace'
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
else:
    pass

## Output F
print('Starting Output F')
user_input = input('Would you like to perform Output F: ')
user_input = user_input.lower()
if user_input == 'y' or user_input =='yes':
    # output each 'read from keyboard' event
    file_path = 'DataSource/LogB.strace'
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
else:
    pass

## Output G
print('Starting Output G')
# output a table for each log counting how many times a file was read
# create a list for file names, counts, timestamps
file_names = []
counts = []
timestamps = []
file_path1 = 'Outputs/ExerciseA-OutputF.txt'
file_path2 = 'Outputs/ExerciseB-OutputE.txt'
user_input = input('Would you like to perform Output G: ')
user_input = user_input.lower()
filename = 'ExerciseA-OutputG.txt'

if user_input == 'y' or user_input =='yes':
    # open the file
    file1=open(file_path1)
    # read content into memory object “lines” 
    lines1=file1.readlines()
    # find file names
    for line in lines1:
        if "read(" in line and "<" in line and ">" in line:
            file_name_start = line.find('<')
            file_name_end = line.find('>')
            file_name = line[file_name_start + 1 : file_name_end]
            # add file names to list
            if file_name not in file_names:
                file_names.append(file_name)
                counts.append(1)
                # Starts list with current time.
                idx = file_names.index(file_name)
                timestamps.append([idx])
            else:
                i = file_names.index(file_name)
                counts[i] += 1
                # add new time
                timestamps[i].append(idx)       
    resultsG=[(file_names[i], counts[i], timestamps[i]) for i in range(len(file_names))]
    
    # output text file
    with open(filename, "a") as f:
        f.write("\n******OutputG*****\n\n")
        f.write("Unique files with one or more 'read from file' events:\n\n")
        # Formats table for Output G
        f.write("{:<50} {:<10} {}\n".format("File Name", "Count", "Timestamps"))
        f.write("-" * 90 + "\n")
        for name, count, times in resultsG:
            f.write("{:<50} {:<10} {}\n".format(name, count, times))
        
    # close the file 
    file1.close()
else:
    pass