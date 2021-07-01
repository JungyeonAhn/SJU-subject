'''
숫자 n을 입력 받고, 집합 s1, s2, s3에 순서대로 각각 n개의 원소를 추가한다.
세 집합 s1, s2, s3의 공통 원소는 제거하고 리스트에 순서대로 저장하여 출력하라.

[입력 예시 1]
4
1
2
3
4
3
4
5
6
3
4
10
11

[출력 예시 1]
List = [1, 2, 5, 6, 10, 11]


[입력 예시 2]
2
1
2
3
4
5
6

[출력 예시 2]
List = [1, 2, 3, 4, 5, 6]
'''
n = int(input())
s1 = []
s2 = []
s3 = []

for i in range(n):
    s1.append(int(input()))

for i in range(n):
    s2.append(int(input()))

for i in range(n):
    s3.append(int(input()))

total_set = set(s1+s2+s3)

List = s1+s2+s3
for i in total_set:
    if List.count(i) == 3:
        while List.count(i):
            List.remove(i)

print("List =", sorted(List))
