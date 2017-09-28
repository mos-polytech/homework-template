massive = [4, 3, 2, -5, 3, 8, 32, 54, 83, -23, 43]

for i in range(0,len(massive)):
    for j in range(0,len(massive)-i-1):
        if massive[j]>massive[j+1]:
            k=massive[j+1]
            massive[j+1]=massive[j]
            massive[j]=k
print(massive);