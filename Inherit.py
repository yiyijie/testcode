#'给出数据文件，想办法用代码找出每个选手最快的三个时间'
import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter1')#'给出打开文件的路径'
os.getcwd()
def sanitize(time_string):#'定义函数'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)#'分割分钟和秒并赋值'
    return(mins + '.' + secs)#"返回分钟和秒中间加'.'号"
#'定义一个类， 继承内置类"list"'
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top(self):
        return(sorted(set([sanitize(each_t) for each_t in self]))[0:3])
def get_coach_data(filename):
    #'增加异常处理'
    try:
        with open(filename) as f:#'打开文件并读取'
            data = f.readline()
        datas = data.strip().split(',')#'给整理好的数据赋值'   
#'用"Athlete'对象创建代码"
        return(AthleteList(datas.pop(0), datas.pop(0), datas))
    except IOError as ioerr:
        print('File error:' + str(ioerr))#'如有异常给出通知并返回None'
        return(None)
    #'下面四行除了调用函数还可以显示储存位置'
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
            #'下面的为 打印每个人所对应的最快时间'
print(james.name + "'s fastest times are:" + str(james.top()))
print(julie.name + "'s fastest times are:" + str(julie.top()))
print(mikey.name + "'s fastest times are:" + str(mikey.top()))
print(sarah.name + "'s fastest times are:" + str(sarah.top()))

#'既然继承了内置类那么"append(),extend()"方法就可以这样直接用了'
#'验证’
vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top())
print(vera)
