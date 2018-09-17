def numbers():
	first_number=int(input())
	second_number=int(input())
	if first_number<0 or second_number<0:
		raise ValueError('You enterd negative number')
	elif first_number%second_number==0:
		return True
	else:
		return False
