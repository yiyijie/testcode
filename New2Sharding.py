import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter1')
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
#'文件增加了姓名生日，上面两个函数用之前的。目的是可以看出每个时间组是属于谁的"
james = get_coach_data('james2.txt')
(james_name, james_dob) = james.pop(0), james.pop(0)
print(james_name + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in james]))[0:3]))
julie = get_coach_data('julie2.txt')
(julie_name, julie_dob) = julie.pop(0), julie.pop(0)
print(julie_name + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in julie]))[0:3]))
mikey = get_coach_data('mikey2.txt')
(mikey_name, mikey_dob) = mikey.pop(0), mikey.pop(0)
print(mikey_name + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in mikey]))[0:3]))
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3]))
