total = 0
num = 0

while True:
    score=int(input('score : '))
    if score==0: break
    total+=score
    num+=1

print('Average =',total//num)
