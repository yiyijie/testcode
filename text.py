import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter3')
os.getcwd()



data = open('sketch.txt')
data.seek(0)
for each_line in data:
    print(each_line, end = '')
