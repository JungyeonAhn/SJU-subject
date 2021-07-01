SW=[]
for i in range(0,8):
    score=int(input('Score = '))
    SW.append(score)
SW=sorted(SW)
SW=reversed(SW)

for i in SW:
    print(i)
