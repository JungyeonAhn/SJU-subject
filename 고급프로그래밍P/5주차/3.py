def sum_digit(n):
    result=0
    while n!=0:
        result=result+n%10
        n=int(n/10)
    return result

n = int(input())
result = sum_digit(n)
print(result)
