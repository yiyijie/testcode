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
#'使用列表推导来完成遍历并排序'
#'注:'sorted(sanitize(each_t)'，不要这样使用,因为函数一次只对一个列表项完成转换，而不是整个列表。'sorted()'希望对一个列表排序，而不是单个数据项
james = sorted([sanitize(each_t) for each_t in james])
julie = sorted([sanitize(each_t) for each_t in julie])
mikey = sorted([sanitize(each_t) for each_t in mikey])
sarah = sorted([sanitize(each_t) for each_t in sarah])

#'删除重复项'
unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])
