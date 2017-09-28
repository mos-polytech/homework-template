li = [4, 1, 5, 2, -2]
j = 1
while j < len(li):
    for i in range(len(li) - j):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
    j = j + 1
