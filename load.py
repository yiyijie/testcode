import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter3')
import pickle#'导入标准模块"pickle"'
import nester#'导入发布模块"nester"'
new_man = []#'创建空列表'
try:
    with open('man_dats.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
          print('Pickling error:' +str(perr))


nester.print_lol(new_man)




print(new_man[0])
print(new_man[-1])
