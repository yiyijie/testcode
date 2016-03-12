
import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter3')

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('the datafile is missing')
                
print(man)
print(other)
import nester
try:
    with open('man_data.txt', 'w') as man_file:#'命名文件名并赋值一个文件对象'
        nester.print_lol(man,True, fh = man_file)#'调用发布的模块函数将指定的列表保存到磁盘文件上'
    with open('other_data.txt', 'w') as other_file:#'同上'
        nester.print_lol(other,True, fh = other_file)#'同上'
except IOError as err:
    print('File error:' + str(err))

    


