def selection_sort(arr):
	for i in range(len(arr) - 1):
		min_index = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_index]:
				min_element = arr[j]
				arr[j] = arr[min_index]
				arr[min_index] = min_element
			j += 1
		i += 1
	print(arr)

arr = [3, 4, 9, 4, 23, 8, 7]
selection_sort(arr)
