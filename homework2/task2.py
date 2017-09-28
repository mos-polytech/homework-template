s = [2, 0, 2, -1, 9]
k = 0

while k < len(s) - 1:
    mm = k
    i = k + 1
    while i < len(s):
        if s[i] < s[mm]:
            m = i
        i += 1
    t = s[k]
    s[k] = s[mm]
    s[mm] = t
    k += 1

print(s)
