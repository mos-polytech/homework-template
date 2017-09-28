list = [9,4,7,0, ]

print(list)
length = len(list)
m = length-1
while m > 0:
    for i in range(m):
        if list[i] > list[i+1]:
            x = list[i]
            list[i] = list[i+1]
            list[i+1] = x
    m = m-1
print(list)

