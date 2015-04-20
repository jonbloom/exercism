def sum_of_multiples(num, multiples=[3,5]):
	_sum = 0
	for i in xrange(num):
		for j in multiples:
			_sum += i if j != 0 and i % j == 0 else 0
	return _sum