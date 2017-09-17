import random

def mergeSort(array):
	
	if len(array) == 1:
		return array

	half = int(len(array)/2)
	arrLeft = array[0:half]
	arrRight = array[half:len(array)]
	sorted_array = [0]*len(array)


	arr1 = mergeSort(arrLeft)
	arr2 = mergeSort(arrRight)

	i = 0; j = 0
	
	for k in range(len(array)):
		
		if i < half and j < half:
			if arr1[i] < arr2[j]:
				sorted_array[k] = arr1[i]
				if i < half:
					i += 1
		
			elif arr1[i] > arr2[j]:
				sorted_array[k] = arr2[j]
				if i < half:
					j += 1

			elif arr1[i] == arr2[j]:
				if i < j:
					sorted_array[k] = arr1[i]
					i += 1
				else:		
					sorted_array[k] = arr2[j]
					j += 1
		elif i < j:
			sorted_array[k] = arr1[i]
			if i < half - 1:
				i += 1
		else:		
			sorted_array[k] = arr2[j]
			if j < half - 1:
				j += 1
			
	return sorted_array

array = [random.randint(0, 9) for _ in range(10000)]

print(array)
print(mergeSort(array))
print(len(array))