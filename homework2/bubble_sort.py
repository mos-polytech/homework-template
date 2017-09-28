list = [1, 5, 6, 7, 1, 0, 10, 15]
n = 1
while n < len(list):
    for i in range(len(list) - n):
	    if list[i] > list[i + 1]:
		    list[i], list[i + 1] = list[i + 1], list[i]
		    print(list)
    n += 1	