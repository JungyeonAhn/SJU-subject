name=input()
fp=open(name,'a')
n=input()
fp.write(n)

fp=open(name,'r')
while True:
    line=fp.readline()
    if not line: break
    print(line)

fp.close()
