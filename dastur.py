def move_zeros_to_end(nums):

	result = []
	zero=0
	for x in nums:
		if x != 0:
			result.append(nums)
		else:
			zero+=1
	for x in range(zero):
		result.append(0)
	return result
if __name__=="__main__":

	numbers = [0, 1, 0, 3, 12]
	print(move_zeros_to_end(numbers))

