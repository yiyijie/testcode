import os
import sys
#需要知道os, sys, path 的路径
def catalog(catalogname):
    lists = []
    filename = os.listdir(catalogname)#获取目录下文件

    for names in filename:#遍历目录下的子文件并添加到列表
        lists.append(len(names))
        #下面是从小到大和从大到小排序并打印
    print(sorted(lists))
    lists.sort(reverse = True)
    print(lists)


catalog('E:/xiaobing/testcode')

