import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter2')
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
        return(data.strip().split(','))#'返回已经处理过空白符和完成分解统一符号'
    except IOError as ioerr:
        print('File error:' + str(ioerr))#'如有异常给出通知并返回None'
        return(None)
#'调用函数'
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

#'1.使用列表推导来完成遍历'
#'2.注:'sorted(sanitize(each_t)'，不要这样使用,因为函数一次只对一个列表项完成转换，而不是整个列表。'sorted()'希望对一个列表排序，而不是单个数据项
#"3.'set'是一个无序集合，这里重要的是它不允许有重复值。  'sorted'排序。 [0:3] 分片前三项"
print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in mikey]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3])
