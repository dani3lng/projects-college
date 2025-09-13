# IST 820 Lab 02 Exercise B

# create output table
# def output_table(filea, fileb, keya, keyb, pipea, pipeb)
print('LogB' + '\t' + '\t' + '\t' + 'A' + '\t' + 'B' + '\n' 
      + 'Read from a file:' + '\t' + 'filea' + '\t' + 'fileb' + '\n'
      + 'Read from a keyboard:' + '\t' + 'keya' + '\t' + 'keyb' + '\n'
      + 'Read from pipe:' + '\t' + '\t' + 'pipea' + '\t' + 'pipeb' + '\n')

# read from file
file_path = ./DataSource/LogB.strace
file1 = open(file_path)
lines = file1.readlines()
file1.close()
