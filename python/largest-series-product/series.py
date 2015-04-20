def slices(numbers, length):
	if len(numbers) < length:
		raise ValueError
	numbers = [int(i) for i in numbers]
	slices = list()
	for i in range(len(numbers)-length+1):
		slices.append(numbers[i:i+length])
	return slices

def largest_product(number, length):
	
	largest = 1

	for s in slices(number, length):
		p = product(s)
		if p > largest:
			largest = p
	return largest

def product(numbers):
	_ = 1
	for number in numbers:
		_ *= number
	return _
