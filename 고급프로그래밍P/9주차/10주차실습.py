'''
딕셔너리 형태로 주어진 학생별 수학 점수 정보{이름 : 점수}**는 아래와 같다.
먼저 추가 혹은 변경할 횟수 N을 입력받고, 이후 각 회차의 추가 혹은 변경을 위한
학생의 수학 점수 정보{key : value}를 입력받는다.
추가 혹은 수정이 모두 완료된 후 딕셔너리에 입력된 모든 학생의 수학 점수 평균을 출력하시오.
(단, 평균 점수는 소수점 둘째 자리까지 반올림하여 출력한다.)
** student = {'Denis' : 60, 'Amin' : 70}

[입력 예시 1]
2
chan
80
Kwon
70

[출력 예시 1]
Average : 70.00


[입력 예시 2]
1
Denis
90

[출력 예시 3]
Average : 80.00

'''
student = {'Denis' : 60, 'Amin' : 70}

n=int(input())
sum1=0
for i in range(0,n):
    name=input()
    student[name]=int(input())

for k in student.values():
    sum1+=k

print('Average : %.2f'%(sum1/len(student)))

