n=int(input('# of students = '))
L=[]
sw=[]
os=[]
db=[]
for i in range(0,n):
    score=input('score = ')
    L=score.split()
    sw.append(int(L[0]))
    os.append(int(L[1]))
    db.append(int(L[2]))

result = sum(sw)
print('Average(SW) = %d'%(result//n))
result = sum(os)
print('Average(OS) = %d'%(result//n))
result = sum(db)
print('Average(DB) = %d'%(result//n))



