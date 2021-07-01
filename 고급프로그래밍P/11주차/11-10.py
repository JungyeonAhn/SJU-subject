city = {}
n = int(input())

for i in range(0,n):
    name=input()
    population=int(input())
    area=int(input())
    city[name]=population/area

dmax=max(city,key=city.get)


print('Highest Population Density = %s'%dmax,', %.2f'%city[dmax])
