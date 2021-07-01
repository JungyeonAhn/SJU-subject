n=int(input("Student Number = "))
s=list()
avg=0
for i in range(0,n):
    Point=int(input("Point = "))
    s.append(Point)
    avg=avg+Point

print(s)
print("%0.2f"%float(avg/n))
