n=int(input('# of person : '))

for i in range(0,n):
    m=int(input('# of dishes : '))
    total=0
    print('person',i+1)
    for j in range(0,m):
        color=input('color : ')
        if color=='white':
            total+=1000
        elif color=='yellow':
            total+=2000
        elif color=='blue':
            total+=3000
        elif color=='red':
              total+=5000
        else: break

    print('Total price of person',i+1,'=',total)
