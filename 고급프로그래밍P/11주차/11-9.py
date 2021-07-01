p = [0, 0, 0]
n = int(input())

for i in range (0,n):
    for j in range(0,3):
        card = int(input('Person%d Card : '%(i+1)))
        if card>p[j]:
            p[j]=card
    print(p)

idx=p.index(max(p))
print('Person%d Win'%(idx+1))
