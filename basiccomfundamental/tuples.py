def getData(aTuple):
  nums=()
  words=()

  for t in aTuple:
    nums = nums + (t[0],)
    if t[1] not in words:
      words = words + (t[1],)
  min_num = min(nums)
  max_num= max(nums)
  uniques= len(words)
  return (min_num,max_num,uniques)

(small,big,words)=getData(((1,"mine"),(3,"yours"),(5,"ours"),(7,"mine")))

print(small)
print(big)
print(words)

# print(small)
# print(big)
# print(words)

#or #=---------------------------------------------------
resultTu = getData(((1,"mine"),(3,"yours"),(5,"ours"),(7,"mine")))

print(resultTu)
#=---------------------------------------------------
for t in resultTu:
  print(t)
#=---------------------------------------------------
for i in range(len(resultTu)):
  print(resultTu[i])
  
#=---------------------------------------------------
small,big,words=getData(((1,"mine"),(3,"yours"),(5,"ours"),(7,"mine")))

print(small)
print(big)
print(words)