import os#'导入模块'
os.getcwd()#'当前目录'
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter3')#'切换包含数据的文件夹'
try:
    data = open('sketch.txt')#'打开"sketch.txt"文本'
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)#'赋值'
            print(role, end = '')
            print(' said: ', end = '')
            print(line_spoken, end = '')
        except ValueError:#'指定要处理错误类型'
            pass

    data.close()#'关闭数据文件'
except IOError:#'指定要处理错误类型'
    print('the data file is missing!')
