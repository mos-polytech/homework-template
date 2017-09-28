def selection_sort(num_list):
    a = num_list
    for i in range(len(a)):
        idxmin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idxmin]:
                idxmin = j
        tmp = a[idxmin]
        a[idxmin] = a[i]
        a[i] = tmp
    return a

	
arr = [1, 8, 4, 10, 7, 3]
print(selection_sort(arr))
