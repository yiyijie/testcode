import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter2')
os.getcwd()
with open('james.txt') as jaf:#'读取文件并赋值数据对象'
    data = jaf.readline()#'读取文本行并只读取一行'
    james = data.strip().split(',')#'新知识点：方法串链'
with open('julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')

    print(james)
    print(julie)
    print(mikey)
    print(sarah)
