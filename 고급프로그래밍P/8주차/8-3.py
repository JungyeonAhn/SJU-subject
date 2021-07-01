user_info = { 'name':'David', 'age':21, 'address':'서울시 광진구' }

n= int(input('수정 횟수 입력 : '))

for i in range (0 , n):
        print('수정 #%d'%(i+1))
        a=input('추가하거나 변경할 key 입력 : ')
        b=input('key 에 대한 값 value 입력 : ')
        user_info[a]=b

print()
print('사용자 정보')

for i in user_info:
    print(i,':',user_info[i])
