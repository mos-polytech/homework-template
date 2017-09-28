s = [2, 0, 2, -1, 9]
k = 0

while k < len(s) - 1:
    min = k
    i = k + 1
    while i < len(s):
        if s[i] < s[min]:
            m = i
        i += 1
    t = s[k]
    s[k] = s[min]
    s[min] = t
    k += 1

print(s)