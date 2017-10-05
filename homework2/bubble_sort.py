num_list = [1, 5, 6, 7, 1, 0, 10, 15]
n = 1
while n < len(num_list):
    for i in range(len(num_list) - n):
	    if num_list[i] > num_list[i + 1]:
		    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
		    print(num_list)
    n += 1	