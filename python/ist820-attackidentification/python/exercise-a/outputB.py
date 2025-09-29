### Exercise A Output A

# variables
filename = 'ExerciseA-OutputB.txt'
stat_pid = None
stat_line_num = None
stat_line = None
clone_pid = None
clone_line_num = None
clone_line = None

# pid function
def pid_from_line(line):
    idx = line.find(' ')
    pid = line[0 : idx]
    return pid

# establish log path
file_path1 = 'data/LogB.strace'
file_path2 = 'data/LogC.strace'
# open the file
file1=open(file_path1)
file2=open(file_path2)
# read content into memory object “lines” 
lines1=file1.readlines()
lines2=file2.readlines()

# textfile header
with open(filename, 'a')  as f:
                f.write("\n******OutputB*****\n\n")
                f.write("'Stat' and 'Clone' Event Sequences:\n\n")

## Log B
# format table for output
with open(filename, 'a') as f:
    f.write("\n******Log B*****\n\n")
    f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
    f.write("-" * 90  )
# find 'stat' and 'clone' events
term1 = ' stat('
term2 = ' clone('
line_num = 1
for line in lines1:
    if term1 in line:
        stat_pid = pid_from_line(line)
        stat_line_num = line_num
        stat_line = line
    elif term2 in line:
        clone_pid = pid_from_line(line)
        clone_line_num = line_num
        clone_line = line
        if clone_pid == stat_pid:
            # output results to console
            print(str(stat_line_num) + '\t' + stat_line)
            print(str(clone_line_num) + '\t' + clone_line)
            # output results to textfile
            with open(filename, 'a')  as f:
                f.write("\n{:<10} {:<10} ".format(stat_line_num, stat_line))
                f.write("{:<10} {:<10} \n".format(clone_line_num, clone_line))
            # clean variables
            stat_pid = None
            stat_line_num = None
            stat_line = None
            clone_pid = None
            clone_line_num = None
            clone_line = None
    line_num += 1        
    
## Log C
# format table for output
with open(filename, 'a') as f:
    f.write("\n******Log C*****\n\n")
    f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
    f.write("-" * 90  )
# find 'stat' and 'clone' events
term1 = ' stat('
term2 = ' clone('
line_num = 1
for line in lines2:
    if term1 in line:
        stat_pid = pid_from_line(line)
        stat_line_num = line_num
        stat_line = line
    elif term2 in line:
        clone_pid = pid_from_line(line)
        clone_line_num = line_num
        clone_line = line
        if clone_pid == stat_pid:
            # output results to console
            print(str(stat_line_num) + '\t' + stat_line)
            print(str(clone_line_num) + '\t' + clone_line)
            # output results to textfile
            with open(filename, 'a')  as f:
                f.write("\n{:<10} {:<10} ".format(stat_line_num, stat_line))
                f.write("{:<10} {:<10} \n".format(clone_line_num, clone_line))
            # clean variables
            stat_pid = None
            stat_line_num = None
            stat_line = None
            clone_pid = None
            clone_line_num = None
            clone_line = None
    line_num += 1    

# close file
file1.close()
file2.close()