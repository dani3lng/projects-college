### Exercise A Output C

# variables
filename = 'ExerciseA-OutputC.txt'
pids = [None, None, None]
line_nums = [None, None, None]
line_strs = [None, None, None]
kw_found = [False, False, False] 

# pid function
def pid_from_line(line):
    idx = line.find(' ')
    pid = line[0 : idx]
    return pid
    
# establish log path
file_path = 'data/LogC.strace'

# open the file
file=open(file_path)

# read content into memory object “lines” 
lines=file.readlines()


# textfile header
with open(filename, 'a')  as f:
                f.write("\n******OutputC*****\n\n")
                f.write("3-stage Event Sequences:\n\n")

# find events in Log X
line_num = 1
for line in lines:
    if 'open(' in line:
        kw_found[0] = True
        pids[0] = pid_from_line(line)
        line_nums[0] = line_num
        line_strs[0] = line
    elif 'getdents(' in line:
        if kw_found[0] == True:
            pid = pid_from_line(line)
            if pid == pids[0]:
                kw_found[1] = True
                pids[1] = pid_from_line(line)
                line_nums[1] = line_num
                line_strs[1] = line 
    elif 'close(' in line:
        if kw_found[1]:
            pid = pid_from_line(line)
            if pid == pids[1]:
                kw_found[2] = True
                pids[2] = pid_from_line(line)
                line_nums[2] = line_num
                line_strs[2] = line
    if kw_found[0] and kw_found[1] and kw_found[2] == True:
        print(line_num, line_strs)
        # # output results to textfile
        # with open(filename, 'a')  as f:
        #     f.write("\n******Log X*****\n\n")
        #     f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
        #     f.write("-" * 90  )
        #     f.write("\n{:<10} {:<10} ".format(line_nums[0], line_strs[0]))
        #     f.write("{:<10} {:<10} \n".format(line_nums[1], line_strs[1])) 
        #     f.write("{:<10} {:<10} \n".format(line_nums[2], line_strs[2])) 
            # clean variables
    pids = [None, None, None]
    line_nums = [None, None, None]
    line_strs = [None, None, None]
    kw_found = [False, False, False]          
    line_num += 1       
# close file
file.close()

