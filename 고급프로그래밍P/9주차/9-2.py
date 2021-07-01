name=input()
fp=open(name,'r')
Total=0

while True:
    line=fp.readline()
    if not line: break
    n= int(line)
    Total+=n

print("Total =",Total)
fp.close()

