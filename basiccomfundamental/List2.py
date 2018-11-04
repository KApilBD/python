aList = [0,1,2,3,4,5]
bList = aList
aList[2] = 'hello'
print(aList == bList)

print(aList is bList)


print(aList)

print(bList)


cList = [6,5,4,3,2]
dList = []

for num in cList:
    dList.append(num)

print(cList == dList) #validate the contain only
print(cList is dList) #validate address

cList[2] = 20
print(cList)

print(dList)
