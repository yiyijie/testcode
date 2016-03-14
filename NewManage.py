import os
os.getcwd()
os.chdir('/SoftWare/python3/libs/headfirstpython/chapter2')
os.getcwd()
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

    clean_james = []
    clean_julie = []
    clean_mikey = []
    clean_sarah = []
#'下面遍历列表并添加到空列表中'
    for each_t in james:
        clean_james.append(sanitize(each_t))
    for each_t in julie:
        clean_julie.append(sanitize(each_t))
    for each_t in mikey:
        clean_mikey.append(sanitize(each_t))
    for each_t in sarah:
        clean_sarah.append(sanitize(each_t))

#'打印并排序列表'
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
