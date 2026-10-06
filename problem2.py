def calculate_dif_sum(set1:set[int],set2:set[int]):
	a = set1.intersection(set2)
	summa = sum(a)
	s = 0
	for x in set1:
		s = s + x
	b = summa - s
	print(summa)
	print(s)
	print(b)
if __name__ == "__main__":
	a = {1,2,3,4,5,6}
	b = {4,5,6,7,8,9}
	calculate_dif_sum(a,b)
