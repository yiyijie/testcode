movies = ['the',1957, 'terry', 91, ['graham',['michael', 'john', 'gilliam', 'eric', 'jones']]]
#""" 这是一个'nester.py'模块，提供一个名为print_lol()的函数，函数的作用是打印列表，其中有可能包含嵌套列表"""
def print_lol(the_list, level = 0):
	#"""'the_list', 是这个函数的位置参数，可以是任何python列表或嵌套列表，所指定的列表中的每个数据项
	#会输出到屏幕上，各数据项各占一行。"""
	#"""'level = 0', 为函数提供一个缺省值"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item, level + 1)
		else:
			for tab_stop in range(level):
				print("\t", end = '')
			print(each_item)
print_lol(movies)