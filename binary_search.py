
def binary_search(A, item):
	if len(A) == 0:
		return False
	else:
		middle = len(A)//2
		if A[middle] == item:
			return True
		elif A[middle] < item:
			new_A = A[middle+1:]
			return binary_search(new_A, item)
		else:
			new_A = A[:middle]
			return binary_search(new_A, item)

list = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search(list, 4))
print(binary_search(list, 42))

