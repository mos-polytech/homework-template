# Сортировка пузырьком
massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43, ]

for i in range(0, len(massive)):
    for j in range(0, len(massive)-i-1):
        if massive[j] > massive[j+1]:
            k = massive[j+1]
            massive[j+1] = massive[j]
            massive[j] = k
print(massive)

# Сложность данной сортировка O(n**2)
# Так как внешний массив проходит n итераций
# А внешний с каждым разом проходит все меньше и меньше (n-1), (n-2)... и тд
# Но округляя получаем n*n, то есть n в квадрате