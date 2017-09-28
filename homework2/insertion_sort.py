list = [5, 0, 3, -1, 4]

for i in range(1, len(list)):
    t = list[i]
    item = i - 1
    while item >= 0 and list[item] > t:
        list[item + 1], list[item] = list[item], t
        item -= 1

print(list)

# Сложность O(n ** 2)
# Каждый элемент из массива берется и вставляется
# в начала или конеч массива.