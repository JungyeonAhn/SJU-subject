name = input()
fp = open(name,"w")

n = int(input())

for i in range(0,n):
    fp.write(str(i+1)+'\n')

fp = open("test.txt","r")
while True:
    line=fp.readline()
    if not line: break
    print(line)
    
fp.close()
