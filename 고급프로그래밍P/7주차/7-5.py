'''
myTuple = (1,9,7,3,2,4,8,5,6)
myList= list(myTuple)
myList.sort()
resultTuple = tuple(myList)
print(resultTuple)
'''

myTuple = (1,9,7,3,2,4,8,5,6)
myList= list(myTuple)

for i in range(len(myList)-1):
    for j in range(len(myList)-1-i):
        if myList[j] > myList[j+1]:
            myList[j], myList[j+1] = myList[j+1], myList[j]

resultTuple = tuple(myList)
print(resultTuple)
