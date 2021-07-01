import random
s=[]
t=[]
for i in range(0,6):
    num=random.randint(1,20)
    s.append(num)


f = open('lotto_num','r')
while True:
    line = f.readline()
    if not line: break
    t.append(int(line))
f.close()



cnt=0

for i in range(0,6):
    for j in range(0,6):
        if s[i]==t[j]:
            cnt+=1
            break

print(s)
print(t)
print('Correct =',cnt)
