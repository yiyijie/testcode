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
#"文件增加新数据，使用字典处理数据"
    #'实现同样的功能，代码也没有减少，有一点就是更容易确定和控制"
james = get_coach_data('james2.txt')
james_a = {}
james_a['name'] = james.pop(0)
james_a['dob'] = james.pop(0)
james_a['times'] = james
print(james_a['name'] + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in james_a['times']]))[0:3]))
julie = get_coach_data('julie2.txt')
julie_a = {}
julie_a['name'] = julie.pop(0)
julie_a['dob'] = julie.pop(0)
julie_a['times'] = julie
print(julie_a['name'] + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in julie_a['times']]))[0:3]))
mikey = get_coach_data('mikey2.txt')
mikey_a = {}
mikey_a['name'] = mikey.pop(0)
mikey_a['dob'] = mikey.pop(0)
mikey_a['times'] = mikey
print(mikey_a['name'] + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in mikey_a['times']]))[0:3]))
sarah = get_coach_data('sarah2.txt')
sarah_a = {}
sarah_a['name'] = sarah.pop(0)
sarah_a['dob'] = sarah.pop(0)
sarah_a['times'] = sarah
print(sarah_a['name'] + "'s fastest times are:" + str(sorted(set([sanitize(each_t) for each_t in sarah_a['times']]))[0:3]))
