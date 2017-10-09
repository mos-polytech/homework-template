f = int(input('Введите число: '))
row = []

for i in range(2, f + 1):
    for j in row:
        if i % j == 0:
            break
        else:
            row.append(i)

print(row)
