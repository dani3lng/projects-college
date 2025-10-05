def pid_from_line(line):
    idx = line.find(' ')
    pid = line[0 : idx]
    return pid

file_path = "data/LogA.strace"
file1 = open(file_path)
lines = file1.readlines()
file1.close()

stat_pid = None
stat_line_num = None
stat_line = None

clone_pid = None
clone_line_num = None
clone_line = None

term='stat('
line_num = 1
for line in lines:
    if term in line:
        stat_pid = pid_from_line(line)
        stat_line_num = line_num
        stat_line = line

    elif 'clone(' in line:
        clone_pid = pid_from_line(line)
        clone_line_num = line_num
        clone_line = line

        if clone_pid == stat_pid:
            print(str(stat_line_num) + '\t' + stat_line)
            print(str(clone_line_num) + '\t' + clone_line)

            stat_pid = None
            stat_line_num = None
            stat_line = None
            clone_pid = None
            clone_line_num = None
            clone_line = None

    line_num += 1
