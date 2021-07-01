a = [5, 2, 4, 1, 3]

for i in range (0,5):
    for j in range(1,5-i):
        if a[j-1]>a[j]:
            tmp=a[j-1]
            a[j-1]=a[j]
            a[j]=tmp

print(a)
