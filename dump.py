
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
import pickle
try:
    with open('man_dats.txt', 'wb') as man_file, open('other_dats.txt', 'wb') as other_file:
        #'命名文件名并赋值一个文件对象'
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('pickle error:', + str(perr)) 

    


