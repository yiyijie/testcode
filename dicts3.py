#'给出数据文件，想办法用代码找出每个选手最快的三个时间'
import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter1')#'给出打开文件的路径'
os.getcwd()
#'定义的函数作用为:转换不一样的符号'
def sanitize(time_string):#'定义函数'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)#'分割分钟和秒并赋值'
    return(mins + '.' + secs)#'返回分钟和秒中间加'.'号'

#'定义一个读取文件并统一符号的函数'
def get_coach_data(filename):
#'增加异常处理'
    try:
        with open(filename) as f:#'打开文件并读取'
            data = f.readline()
        datas = data.strip().split(',')#'给整理好的数据赋值'
        #‘下面一行代码：具体为 先在创建函数之前创建一个临时列表存放数据，如"name", "dob", "times", 然后创建了函数，为避免较多的重复代码'
        return({'name' : datas.pop(0), 'dob' : datas.pop(0), 'times' : str(sorted(set([sanitize(each_t) for each_t in datas]))[0:3])})
    except IOError as ioerr:
        print('File error:' + str(ioerr))#'如有异常给出通知并返回None'
        return(None)
#'下面四行代码为创建的四个字典'
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
#'下面的为 打印每个人所对应的最快时间'
print(james['name'] + "'s fastest times are:" + james['times'])
print(julie['name'] + "'s fastest times are:" + julie['times'])
print(mikey['name'] + "'s fastest times are:" + mikey['times'])
print(sarah['name'] + "'s fastest times are:" + sarah['times'])
