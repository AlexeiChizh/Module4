

a = [23, 5, 56, 67, 4, 54, 1, 0]

def insert(a):
	for i in range(len(a)):
		j = i - 1
		key = a[i]

		while a[j] > key and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key
	return a
print(a)
print(insert(a))

