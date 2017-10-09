f = int(input("Введите число: "))
s = int(input("Введите число: "))
r = []

for i in range(f,s+1):
    if i%5==0:
	    r.append(i)

print(r)