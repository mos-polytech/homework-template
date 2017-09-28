def sort1(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]

arr = [5, 1, 4, 2, 8,]
print(sort1(arr))

# Сложность O(n^2)
# Алгоритм сравнивает сорседние элементы массива, и если нужно, меняет их местами
# В худшем случае, когда все элементы массива стоят в обратном порядке
# Число операций будет равно (N-1)*N/2