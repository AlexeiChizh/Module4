# итерационный метод


m = [1, 23, 13, 45, 123, 0, 67, 11, 3,]
number = 45
a = sorted(m)


def binary(a, number):
	first = 0
	last = len(a) - 1
	while first <= last:
		middle = first + (last - first) // 2
		if a[middle] == number:
			return middle
		elif a[middle] < number:
			first = middle + 1
		else:
			last = middle - 1
			return - 1
print(binary(a, number))