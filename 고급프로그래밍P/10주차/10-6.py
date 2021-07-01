subject={'SW', 'DB', 'OS', 'DS', 'AI', 'CG', 'SE', 'HCI'}
sub=[]
selected=[]
for i in range(0,8):
    s=input()
    sub=s.split()
    selected.extend(sub)

selected=set(selected)

print('Selected Subjects =',selected)
print('Deleted Subjects =',subject-selected)


'''
SW DB OS
DS AI
DS SW CG
SW OS DS CG
CG SE
AI DB SW
OS DS
SW
'''
