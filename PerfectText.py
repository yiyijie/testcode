import os#'导入模块'
os.getcwd()#'当前目录'
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter3')#'切换包含数据的文件夹'
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')#'打开"sketch.txt"文本'
    for each_line in data:
        if not each_line.find(':') == -1:#'如果"each_line"文本行找得到":"'
            (role, line_spoken) = each_line.split(':', 1)#'赋值'
            print(role, end = '')
            print(' said: ', end = '')
            print(line_spoken, end = '')
    data.close()#'关闭数据文件'
else:
    print('the data file is missing!')
