def count_factors(n):
    cnt=1
    for i in range(1,n+1):
        if n%i==0:
            cnt=cnt+1
    return cnt

n = int(input())
result = count_factors(n)
print(result)
