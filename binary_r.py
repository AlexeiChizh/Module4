# рекурсивный метод

m = [1, 23, 13, 45, 123, 0, 67, 11, 3,]
number = 13
a = sorted(m)

def binary_r(a, number, first, last):

	if last >= first:
		middle = first + (last - first) // 2

		if a[middle] == number:
			return middle

		elif a[middle] < number:
			return binary_r(a, number, middle + 1, last)

		else:
			return(a, number, first, middle - 1)
			return - 1
print(binary_r(a, number, 0, len(a) - 1))
