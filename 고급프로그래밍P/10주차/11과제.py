dic={}

while True: 
    key=input()
    if key=='0': break
    value=input()
    dic[key]=value

sdic=sorted(dic.items())
dic=dict(sdic)

print("VALUE is ",end='')
for i in dic:
    print(dic[i],'',end='')
