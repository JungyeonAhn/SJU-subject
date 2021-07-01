import random

card={}
s=[]
total=0
while total<=17:
    num=random.randint(0,10)
    total+=num
    s.append(num)

card['Player1']=s

print("Player1's Card =",card['Player1'])
print(total)
