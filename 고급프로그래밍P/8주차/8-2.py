user_info = { 'name':'David', 'age':21, 'address':'서울시 광진구' }

a= input('원하는 정보 : ')

if a in user_info:
    print(a,':',user_info[a])
else:
    print('해당되는 정보가 존재하지 않습니다.')
