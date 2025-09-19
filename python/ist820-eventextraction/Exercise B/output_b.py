### Exercise B Output B

# create list for program names
program_exec_loga = []
program_exec_logb = []
program_write_loga = [] 
program_write_logb = [] 
program_getfile_loga = [] 
program_getfile_logb = [] 
program_unlink_loga = [] 
program_unlink_logb = [] 
program_end_loga = [] 
program_end_logb = [] 

# name = input('Name text file: ')
print('Starting Output A')
# set file paths for logs
file_path1 = 'DataSource/LogA.strace'
file_path2 = 'DataSource/LogB.strace'
# open the log files
file1=open(file_path1)
file2=open(file_path2)
# read logs content into memory object “lines” 
lines1=file1.readlines()
lines2=file2.readlines()
# close the file 
file1.close()
file2.close()

# events to find in data logs
term1=' execve('
term2=' write('
term3=' access('
term4=' stat('
term5=' unlinkat('
term6=' exit_group('

# find term1 in Logs
for line in lines1:
      if term1 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_exec_loga.append(name)
            programexec_logalen= len(program_exec_loga)
for line in lines2:
      if term1 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_exec_logb.append(name) 
            programexec_logblen = len(program_exec_logb)

# find term2 in Logs
for line in lines1:
      if term2 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_write_loga.append(name)
            programwrite_logalen = len(program_write_loga)
for line in lines2:
      if term2 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_write_logb.append(name) 
            programwrite_logblen = len(program_write_logb)
            
# find term3 in Logs
for line in lines1:
      if term3 in line or term4 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_getfile_loga.append(name) 
            programget_logalen = len(program_getfile_loga)
for line in lines2:
      if term3 in line or term4 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_getfile_logb.append(name) 
            programget_logblen = len(program_getfile_logb)
            
# find term5 in logs
for line in lines1:
      if term5 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_unlink_loga.append(name) 
            programunlink_logalen = len(program_unlink_loga)
for line in lines2:
      if term5 in line:
            position_a = line.find("'")
            position_b = line.find("'", position_a + 1)
            name = line[position_a + 1 : position_b]
            program_unlink_logb.append(name) 
            programunlink_logblen = len(program_unlink_logb)
            
# create output table
print(f"""Event                                           LogA    LogB
Total number of 'a program starts running':     {programexec_logalen}     {programexec_logblen}
Total number of 'write events':                 {programwrite_logalen}    {programwrite_logalen}
Total number of 'get file/directory status':    {programget_logalen}      {programget_logblen}
Total number of 'file unlinking':               {programunlink_logalen}   {programunlink_logblen} """)



# Read from pipe:       {loga_pipetotal}     {logb_pipetotal}""", file=open(name, 'a'))
