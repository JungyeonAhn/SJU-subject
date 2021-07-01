n=int(input('# of sushi = '))
sushi={'salmon roe':1000,'red sea bream':3000,'egg roll':1000,'shrimp':2000,
       'kimbab':1000,'tuna':5000}
total=0
for i in range(0,n):
       name=input('name = ')
       total+=sushi[name]

print('Total price = ',total)
