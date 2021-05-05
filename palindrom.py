def palindrom(_str, i):

	if (i < int(len(_str) / 2)):
		if(_str[i] != _str[len(_str) -i-1]):
			print('0')
		else:
			return palindrom(_str, i+1)
	else:
		print('1')


x = input('Type string: ')
palindrom(x, 0)
