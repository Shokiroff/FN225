def add_p(lst: list, prefix: str) -> list[str]:
	result = []

	for x in lst:
		result.append(prefix + str(x))

	return result

print(add_p([1, 2, 3, 4], 'emp'))

