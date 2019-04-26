#coding=utf-8

def add_all_nums(*args):
	'''
	tuple & list unpacking
	'''
	total = 0
	for num in args:
		total += num
	return total



def say_hi(first, second):
	'''
	dictionary unpacking
	'''
	print '{} say hi to {}'.format(first, second)



def unpacking(a, b, c, **kwargs):
	'''
	unpacking & **kwargs
	'''
	print kwargs
	print a + b * c
	print 'leftover...'
	print kwargs


if __name__ == '__main__':
	'''
	tuple & list unpacking
	'''
	print add_all_nums(1,2,3,4,5,6,7,8,9)
	list1 = [1,2,3,4,5,6,7,8,9]
	tuple1 = (1,2,3,4,5,6,7,8,9)
	# add_all_nums(list1) #erro
	# add_all_nums(tuple1) #erro
	print add_all_nums(*list1)
	print add_all_nums(*tuple1)
	'''
	dictionary unpacking
	'''
	names = dict(first = 'ted', second = 'robin')
	print names
	say_hi(**names) # dictionary unpacking
	say_hi(names['first'], names['second'])
	say_hi(first = 'ted', second = 'robin')
	# say_hi(names) # erro

	'''
	unpacking & **kwargs
	'''
	dictionary = dict(a = 1, b = 2, c = 3, d = 4, name = 'tony')
	unpacking(**dictionary)

