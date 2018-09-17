def numbers():
	first_number=int(input())
	second_number=int(input())
	list_numbers=[]
	if first_number<0 or second_number<0:
		raise ValueError('You entered negative number')
	for i in range(first_number,second_number+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			list_numbers.append(i)
	print(list_numbers)
	if len(list_numbers)==0:
		print('Error: NoSimpleDigits')
