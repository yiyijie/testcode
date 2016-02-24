fav_movies = ['the holy frail', 'the lifw of brian']
print(fav_movies[0])
print(fav_movies[1])
for each_flick in fav_movies:
	print(each_flick)


count = 0
while count < len(fav_movies):
	print(fav_movies[count])
	count += 1


movies = ['the holy grail',1975,'terry jones terry filliam',91,['graham chapman',['jie', 'qiang', 'fei']]]
print(movies[4][1][2])
for item in movies:
	if isinstance(item, list):
		for name in item:
			if isinstance(name, list):
				for num in name:
					print(num)
			else:
				print(name)
	else:
		print(item)


def isList(the_list):
	for items in the_list:
		if isinstance(items,list):
			isList(items)
		else:
			print(items)

print(isList(movies))
