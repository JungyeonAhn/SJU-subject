SW = [ 'SW', 'OS', 'DB', 'DS' ]
CS = [ 'SW', 'AI', 'CG', 'HCI' ]

set1=set(SW)
set2=set(CS)

print('1. ‘OS’가 SW 학과 과목인가요? (True/False)')
print('2. ‘OS’가 CS 학과 과목이 아닌가요? (True/False)')
print('3. SW학과 CS학과 공통 과목 출력')
print('4. SW학과 CS학과 통합 과목 출력')
print('5. SW에만 있고 CS에는 없는 과목 출력')

if 'OS' in SW:
    print('True')
if 'OS' not in CS:
    print('True')
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
