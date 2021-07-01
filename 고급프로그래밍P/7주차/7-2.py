score=[[],[],[]]

for i in range(0,3):
    for j in range(0,8):
        score[i].append(int(input()))
print(score)

for i in range(3):
    print("Min["+str(i)+"] =",min(score[i]))


'''
90
80
100
70
80
90
100
90
60
30
90
90
85
80
75
70
85
60
99
100
90
80
70
60
'''
