def sort(num_list):
    for i in range(1, len(num_list)):
        last = num_list[i]
        k = i - 1
        while k >= 0:
            if num_list[k + 1] < num_list[k]:
                num_list[k + 1] = num_list[k]
                num_list[k] = num_list
                k = k - 1
            else:
                break
				
				
numb_list = [1, 7, 5, 1, 6, 8, 15, 20, 3, 4]
sort(numb_list)
print(numb_list)
