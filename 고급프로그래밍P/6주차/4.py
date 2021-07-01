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
