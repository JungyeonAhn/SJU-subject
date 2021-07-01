'''1'''
num=int(input("num = "))
result=0
while num>0:
    result=result+num%10
    num=int(num/10)

print("Result = ",result)

'''2'''
n=int(input("Student Number = "))
s=list()
avg=0
for i in range(0,n):
    Point=int(input("Point = "))
    s.append(Point)
    avg=avg+Point
print(s)
print("%0.2f"%float(avg/n))


'''3'''
for i in range (1,6):
    for j in range (0,i):
        print(i,end='')
    print()


'''4'''
s=list()
avg=0
cnt=0
while True:
    Point=int(input("Point = "))
    if Point==0:
        break
    s.append(Point)
    avg=avg+Point
    cnt+=1
print(s)
print("%0.2f"%float(avg/cnt))


'''5'''
s=[0,1,2,3,4,5,6,7,8,9]
index=int(input("Index = "))
num=int(input("Number = "))
s[index]=num
print(s)


'''6'''
p=[0,0,0]
n=int(input())

for i in range (1,n+1):
    card1=int(input("Person1 Card = "))
    if card1>p[0]:
        p[0]=card1
        
    card2=int(input("Person2 Card = "))
    if card2>p[1]:
        p[1]=card2
        
    card3=int(input("Person3 Card = "))
    if card3>p[2]:
        p[2]=card3
        
    print(p)
    
print("Person",p.index(max(p))+1," Win")

