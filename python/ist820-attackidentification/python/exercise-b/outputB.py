### Exercise B Output B

# variables
filename = 'ExerciseB-OutputB.txt'
term1 = ' open('
term2 = 'fchmodat('

# pid function
def pid_from_line(line):
    idx = line.find(' ')
    pid = line[0 : idx]
    return pid

# textfile header
with open(filename, 'a')  as f:
    f.write("\n******OutputB*****\n\n")
    f.write("'Modify Permission' Event Sequences:\n\n")

# find events in Log A
def logA(lines1):
    pids = [None, None]
    line_nums = [None, None]
    line_strs = [None, None]
    kw_found = [False, False] 
    line_num = 1
    with open(filename, 'a')  as f:
        f.write("\n******Log A******\n")
        f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
        f.write("-" * 90  )
    for line in lines1:
        if term1 in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif term2 in line:
            print(line)
            if kw_found[0]:
                pid = pid_from_line(line)
                if pid == pids[0]:
                    kw_found[1] = True
                    pids[1] = pid_from_line(line)
                    line_nums[1] = line_num
                    line_strs[1] = line 
                    if kw_found[0] and kw_found[1] == True:
                        print(line_num, line_strs)
                        # # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None]
                        line_nums = [None, None]
                        line_strs = [None, None]
                        kw_found = [False, False]        
        line_num += 1        

# find events in Log B
def logB(lines2):
    pids = [None, None]
    line_nums = [None, None]
    line_strs = [None, None]
    kw_found = [False, False] 
    line_num = 1
    with open(filename, 'a')  as f:
        f.write("\n******Log B******\n")
        f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
        f.write("-" * 90  )
    for line in lines2:
        if term1 in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif term2 in line:
            print(line)
            if kw_found[0]:
                pid = pid_from_line(line)
                if pid == pids[0]:
                    kw_found[1] = True
                    pids[1] = pid_from_line(line)
                    line_nums[1] = line_num
                    line_strs[1] = line 
                    if kw_found[0] and kw_found[1] == True:
                        print(line_num, line_strs)
                        # # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None]
                        line_nums = [None, None]
                        line_strs = [None, None]
                        kw_found = [False, False]        
        line_num += 1

# find events in Log C
def logC(lines):
    pids = [None, None]
    line_nums = [None, None]
    line_strs = [None, None]
    kw_found = [False, False] 
    line_num = 1
    with open(filename, 'a')  as f:
        f.write("\n******Log C******\n")
        f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
        f.write("-" * 90  )
    for line in lines:
        if term1 in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif term2 in line:
            print(line)
            if kw_found[0]:
                pid = pid_from_line(line)
                if pid == pids[0]:
                    kw_found[1] = True
                    pids[1] = pid_from_line(line)
                    line_nums[1] = line_num
                    line_strs[1] = line 
                    if kw_found[0] and kw_found[1] == True:
                        print(line_num, line_strs)
                        # # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None]
                        line_nums = [None, None]
                        line_strs = [None, None]
                        kw_found = [False, False]        
        line_num += 1
        
## establish log path
file_path1 = 'data/LogA.strace'
file_path2 = 'data/LogB.strace'
file_path3 = 'data/LogC.strace'
file1=open(file_path1)
file2=open(file_path2)
file3=open(file_path3)
lines1=file1.readlines()
lines2=file2.readlines()
lines3=file3.readlines()
file1.close()
file2.close()
file3.close()

## main
logA(lines1)
logB(lines2)
logC(lines3)