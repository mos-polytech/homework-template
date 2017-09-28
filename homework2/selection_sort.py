#Сортировка выборкой
massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43]
imaxnow = 0
while imaxnow < len(massive) - 1:
    min = imaxnow
    i = imaxnow + 1
    while i < len(massive):
        if massive[i] < massive[min]:
            min = i
        i += 1
    massive[imaxnow], massive[min] = massive[min], massive[imaxnow]
    imaxnow += 1

print(massive)

# Сложность данной сортировки тоже O(N**2)
# Два цикла, оба в худшем случае проходят n инетраций
# А это значит, что сложность сортировки n*n, то есть n в кввадрате
