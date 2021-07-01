Grade = [
['C', 'B', 'A', 'C', 'D'],
['F', 'D', 'C', 'D', 'B'],
['A', 'B', 'A', 'B', 'A'],
['A', 'A', 'B', 'C', 'D'],
['B', 'B', 'B', 'B', 'B'],
['B', 'B', 'C', 'D', 'F'],
['C', 'A', 'A', 'A', 'A'],
['D', 'A', 'A', 'C', 'F'] ]

dic={'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0.0}
student=[]

for i in range(0,8):
    total=0.0
    if Grade[i][0] in dic:
        total+=dic[Grade[i][0]]*3
    if Grade[i][1] in dic:
        total+=dic[Grade[i][1]]*3
    if Grade[i][2] in dic:
        total+=dic[Grade[i][2]]*3
    if Grade[i][3] in dic:
        total+=dic[Grade[i][3]]*2
    if Grade[i][4] in dic:
        total+=dic[Grade[i][4]]*1
    student.append(float(total/12))


for i in range(0,len(student)):
    print(i,'= %.2f'%student[i])
