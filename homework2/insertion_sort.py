def sort(list):
    for i in range(1, len(list)):
        last = list[i]
        k = i - 1
        while k >= 0:
            if list[k + 1] < list[k]:
                list[k + 1] = list[k]
                list[k] = last
                k = k - 1
            else:
                break
numb_list = [1, 7, 5, 1, 6, 8, 15, 20, 3, 4]
sort(numb_list)
print(numb_list)