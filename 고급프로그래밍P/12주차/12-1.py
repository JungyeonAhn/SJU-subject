import random

f = open('lotto_num','w')

for i in range(0,6):
    num = random.randint(1,20)
    f.write("%d\n"%num)
f.close()


f = open('lotto_num','r')

while True:
    line = f.readline()
    if not line: break
    print(int(line)) '''int를 넣으면 \n이 빠짐!!'''
f.close()
