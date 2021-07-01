s =[8, 6, 9, 10, 4, 7, 10, 6, 8, 7]


print("Max = ",max(s))
idx=0
for i in s:
    if i==max(s):
        break
    idx=idx+1
print("Idx = ",idx)
