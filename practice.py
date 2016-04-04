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
    (mins, secs) = time_string.split(splitter)#'分割分钟和秒并赋值'#'返回分钟和秒中间加'.'号'
    return(mins, '+' + secs)




mine = [1, 2, 3]
sece = [m * 60 for m in mine]
print(sece)



meters = [1 ,10, 3]
feet = [m * 3.281 for m in meters]
print(feet)


lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)



