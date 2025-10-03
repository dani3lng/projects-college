### Exercise B Output A

# variables
filename = 'ExerciseB-OutputA.txt'
term1 = ' stat('
term2 = ' clone('
term3 = ' close('

# pid function
def pid_from_line(line):
    idx = line.find(' ')
    pid = line[0 : idx]
    return pid

# textfile header
with open(filename, 'a')  as f:
    f.write("\n******OutputA*****\n\n")
    f.write("'Download malicious code' Event Sequences:\n\n")
    # Format table for output
    f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
    f.write("-" * 90  )

# find events in LogA
def logA(lines1):
    pids = [None, None, None]
    line_nums = [None, None, None]
    line_strs = [None, None, None]
    kw_found = [False, False, False] 
    line_num = 1
    for line in lines1:
        if 'open(' in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif 'write(' in line:
            if kw_found[0]:
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
                        # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n******Log A*****\n")
                            f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
                            f.write("-" * 90  )
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None, None]
                        line_nums = [None, None, None]
                        line_strs = [None, None, None]
                        kw_found = [False, False, False]        
        line_num += 1        

# find events in LogB
def logB(lines2):
    pids = [None, None, None]
    line_nums = [None, None, None]
    line_strs = [None, None, None]
    kw_found = [False, False, False] 
    line_num = 1
    for line in lines2:
        if 'open(' in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif 'write(' in line:
            if kw_found[0]:
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
                        # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n******Log B*****\n")
                            f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
                            f.write("-" * 90  )
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None, None]
                        line_nums = [None, None, None]
                        line_strs = [None, None, None]
                        kw_found = [False, False, False]        
        line_num += 1
        
# find events in LogC
def logC(lines3):
    pids = [None, None, None]
    line_nums = [None, None, None]
    line_strs = [None, None, None]
    kw_found = [False, False, False] 
    line_num = 1
    for line in lines3:
        if 'open(' in line:
            kw_found[0] = True
            pids[0] = pid_from_line(line)
            line_nums[0] = line_num
            line_strs[0] = line
        elif 'write(' in line:
            if kw_found[0]:
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
                        # output results to textfile
                        with open(filename, 'a')  as f:
                            f.write("\n******Log B*****\n")
                            f.write("{:<10} {:<10} \n".format("Timestamp", "Log Entry"))
                            f.write("-" * 90  )
                            f.write("\n{:<10} {:<5} ".format(line_nums[0], line_strs[0]))
                            f.write("{:<10} {:<5}".format(line_nums[1], line_strs[1])) 
                            f.write("{:<10} {:<5}".format(line_nums[2], line_strs[2])) 
                        # clean variables
                        pids = [None, None, None]
                        line_nums = [None, None, None]
                        line_strs = [None, None, None]
                        kw_found = [False, False, False]        
        line_num += 1
                
# establish log path
file_path1 = 'data/LogA.strace'
file_path2 = 'data/LogB.strace'
file_path3 = 'data/LogC.strace'
# open the file
file1=open(file_path1)
file2=open(file_path2)
file3=open(file_path3)
# read content into memory object “lines” 
lines1=file1.readlines()
lines2=file2.readlines()
lines3=file3.readlines()
# close file
file1.close()
file2.close()
file3.close()

# run log scans
logA(lines1)
logB(lines2)
logC(lines3)
