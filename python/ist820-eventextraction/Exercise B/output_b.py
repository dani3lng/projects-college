### Exercise B Output B

## variables
# total 'a program start running' counter
loga_programstart = 0
logb_programstart = 0
# 'write events' counter
loga_write = 0
logb_write = 0
# total 'get file/directory status' counter
loga_filestatus = 0
logb_filestatus = 0
# total 'file unlinking' counter
loga_unlink = 0
logb_unlink = 0
# total 'a program ends executing' counter
loga_programends = 0
logb_programends = 0

# create list for program names
program_exec = [] 
program_write = [] 
program_getfile = [] 
program_unlink = [] 
program_end = [] 

name = input('Name text file: ')
print('Starting Output A')
# set file paths for logs
file_path1 = 'DataSource/LogA.strace'
# file_path2 = 'DataSource/LogB.strace'
# open the log files
file1=open(file_path1)
# file2=open(file_path2)
# read logs content into memory object “lines” 
lines1=file1.readlines()
# lines2=file2.readlines()
# close the file 
file1.close()
# find events in data logs
term1=' execve('
term2=' write('
term3=' access('
term4=' stat('
term5=' unlinkat('
term6=' exit_group('
# find terms in LogA
for line in lines1:
      if term1 in line:
            position_a = line.find('"')
            position_b = line.find('"', position_a + 1)
            name = line[position_a + 1 : position_b]
            program_exec.append(name)
      if term1 in line:
            position_a = line.find('”')
            position_b = line.find('"', position_a + 1)
            name = line[position_a + 1 : position_b]
            program_exec.append(name) 

print(program_exec)
# # create output table
# print(f"""Event                 LogA    LogB
# Total number of 'a program starts running':     {loga_readtotal}     {logb_readtotal}
# Read from a keyboard: {loga_keytotal}     {logb_keytotal}
# Read from pipe:       {loga_pipetotal}     {logb_pipetotal}""", file=open(name, 'a'))

# close the file 
file1.close()
# file2.close()

