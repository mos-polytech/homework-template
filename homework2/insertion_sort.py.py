list = [5,52,3,1,9,6,7,]
print(list)
for i in range(len(list)):
        num = list[i]
        index = i;
        while (list[index-1] > num) and (index > 0):
            list[index] = list[index-1]
            index = index - 1
        list[index] = num
print(list)