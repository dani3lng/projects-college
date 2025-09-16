## Output G
print('Starting Output G')
# output a table for each log counting how many times a file was read
# create a list for file names and counts
file_names = []
counts = []
file_path = 'ist820-eventextraction/Outputs/ExerciseA-OutputE.txt'
# open the file
file1=open(file_path)
# read content into memory object “lines” 
lines=file1.readlines()
for line in lines:
    # find file names
    file_name_start = line.find('<')
    file_name_end = line.find('>')
    file_name = line[file_name_start + 1 : file_name_end]
    # add file names to list
    if file_name not in file_names:
        file_names.append(file_name)
    # # add to counts      
    # if file_name in file_names:  
    #     idx = file_names.index(file_name)
    #     print(idx)
    #     # counts[idx] += 1      
print(file_names)
print(counts)


#     # create file counter
#         idx = file_names.index(file_name)
#         counts[idx] += 1
# print(f'File Name    |    Counts')
# for i in range(len(file_names)):
#     print(file_name + '\n' + '\n' + counts)
# # close the file 
# file1.close()