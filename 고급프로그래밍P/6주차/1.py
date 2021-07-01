num=int(input("num = "))
result=0
while num>0:
    result=result+num%10
    num=int(num/10)

print("Result = ",result)
