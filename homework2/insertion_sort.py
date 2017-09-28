lis = [5, 0, 3, -1, 4]

for i in range(1, len(lis)):
    t = lis[i]
    item = i - 1
    while item >= 0 and lis[item] > t:
        lis[item + 1], lis[item] = lis[item], t
        item -= 1

print(lis)

# Сложность O(n ** 2)
# Каждый элемент из массива берется и вставляется
# в начала или конеч массива.
