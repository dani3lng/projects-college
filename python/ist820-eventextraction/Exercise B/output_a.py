### Exercise B Output A

# LogA total variables
loga_readtotal = 0
loga_keytotal = 0
loga_pipetotal = 0
# LogB total variables
logb_readtotal = 0
logb_keytotal = 0
logb_pipetotal = 0
# name variable for text file
name = input('Name text file: ')

print('Starting Output A')
# set file paths for logs
file_path1 = 'DataSource/LogA.strace'
file_path2 = 'DataSource/LogB.strace'
# open the file LogA
file1=open(file_path1)
# read LogA content into memory object “lines” 
lines=file1.readlines()
# find read, key, pipe LogA events
term1=' read('
term2='tty'
term3='pipe'
for line in lines:
      if term1 in line:
            loga_readtotal += 1
for line in lines:
      if term2 in line:
            loga_keytotal += 1
for line in lines:
      if term3 in line:
            loga_pipetotal += 1
            
# open the file LogB
file2=open(file_path2)
# read LogB content into memory object “lines” 
lines=file2.readlines()
# find read, key, pipe LogA events
for line in lines:
      if term1 in line:
            logb_readtotal += 1
for line in lines:
      if term2 in line:
            logb_keytotal += 1
for line in lines:
      if term3 in line:
            logb_pipetotal += 1

# create output table
print(f"""Event                 LogA    LogB
Read from a file:     {loga_readtotal}     {logb_readtotal}
Read from a keyboard: {loga_keytotal}     {logb_keytotal}
Read from pipe:       {loga_pipetotal}     {logb_pipetotal}""", file=open(name, 'a'))

# close the file 
file1.close()
file2.close()

