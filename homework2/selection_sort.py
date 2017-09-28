# Сортировка выборкой
massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43]
max_elem = 0
while max_elem < len(massive) - 1:
    min_elem = max_elem
    i = max_elem + 1
    while i < len(massive):
        if massive[i] < massive[min_elem]:
            min_elem = i
        i += 1
    massive[max_elem], massive[min_elem] = massive[min_elem], massive[max_elem]
    max_elem += 1

print(massive)

# Сложность данной сортировки тоже O(N**2)
# Два цикла, оба в худшем случае проходят n инетраций
# А это значит, что сложность сортировки n*n, то есть n в кввадрате
