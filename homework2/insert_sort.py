# Сортировка вставками
massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43]
for i in range(0,len(massive)):  
    j = i
    while (j>0) and (massive[j - 1] > massive[j]):
               massive[j - 1], massive[j] = massive[j], massive[j - 1]
               j -= 1
print(massive)

# Сортировка вставками имеет сложность O(n**2)
# Количество сравнений вычисляется по формуле n*(n-1)/2 
# Округляя получается n**2 
