user_info = { 'id':'software', 'pw':'python' }

a=input('Input ID :')
b=input('Input Pw :')

if a!=user_info['id'] :
    print("ID Mismatch!")
elif b!=user_info['pw']:
    print('PW Mismatch!')
else:
    print("success")
