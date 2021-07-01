import random

s=[]
for i in range(0,2):
    num = random.randint(1,10)
    s.append(num)

print("Player1's card =",s)
total=sum(s)
while total<=21:
    n=int(input())
    if n==0: break
    elif n==1:
        num = random.randint(1,10)
        s.append(num)
        print("Player1's card =",s)
        total=sum(s)
        
total=sum(s)
print('Total =',total)
if total>21:
    print('Lose')

    

