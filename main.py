dict_files = {}
list_len = []
with open ('1.txt', encoding = 'utf-8') as file1:
    lines1 = file1.readlines()
    i1 = len(lines1)
with open ('2.txt', encoding = 'utf-8') as file2:
    lines2 = file2.readlines()
    i2 = len(lines2)
with open ('3.txt', encoding = 'utf-8') as file3:
    lines3 = file3.readlines()
    i3 = len(lines3)
list_len.append(i1)
list_len.append(i2)
list_len.append(i3)
list = sorted(list_len)
dict_files ['1.txt'] = i1
dict_files ['2.txt'] = i2
dict_files ['3.txt'] = i3
# print(list)
# print(dict_files)
with open ('4.txt' , 'a') as file4:
    for all in list:
        for key,value in dict_files.items():
            if value == all:
                file4.write (f'{key} \n')
                file4.write (f'{str(all)} \n')
                with open(key, encoding = 'utf-8') as xfile:
                    lines = xfile.readlines()
                    for line in lines:
                        file4.write(f'{str(line)} \n')
