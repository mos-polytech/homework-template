# Сортировка выборкой
massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43]
max_element = 0
while max_element < len(massive) - 1:
    min_element = max_element
    i = max_element + 1
    while i < len(massive):
        if massive[i] < massive[min_element]:
            min_element = i
        i += 1
    massive[max_element], massive[min_element] = massive[min_element], massive[max_element]
    max_element += 1

print(massive)

# Сложность данной сортировки тоже O(N**2)
# Два цикла, оба в худшем случае проходят n инетраций
# А это значит, что сложность сортировки n*n, то есть n в кввадрате
