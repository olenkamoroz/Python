old_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
>>> new_list=[]
>>> def lists(old_list):
	for i in old_list:
		if type(i)==list:
			lists(i)
		else:
			new_list.append(i)
