def slices(numbers, length):
	if len(numbers) < length < 1:
		raise ValueError
	numbers = [int(i) for i in numbers]
	slices = list()
	for i in range(len(numbers)-length+1):
		slices.append(numbers[i:i+length])
	return slices