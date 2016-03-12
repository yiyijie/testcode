import sys

#""" 这是一个'nester.py'模块，提供一个名为print_lol()的函数，函数的作用是打印列表，其中有可能包含嵌套列表"""
def print_lol(the_list, indent = False, level = 0, fh = sys.stdout):
	#"""'the_list', 是这个函数的位置参数，可以是任何python列表或嵌套列表，所指定的列表中的每个数据项
	#会输出到屏幕上，各数据项各占一行。"""
	#"""'level = 0', 为函数提供一个缺省值"""
	#'indent'参数值可以控制缩进
        #'sys.stdout'标识将把数据写入哪个位置
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item, indent, level + 1, fh)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t', end = ' ', file = fh)
			print(each_item, file = fh)
