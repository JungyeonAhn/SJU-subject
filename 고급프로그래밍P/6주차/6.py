p=[0,0,0]
n=int(input())

for i in range (1,n+1):
    for j in range (0,3):
        card=int(input("Person"+str(j+1)+"Card = "))
        if card>p[j]:
            p[j]=card
    print(p)
        

print("Person",p.index(max(p))+1," Win")
