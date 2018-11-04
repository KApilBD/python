L=[2,1,3]
print(L )
L[1] = 5

print(L)

x = [1, 2, [3, 'John', 4], 'Hi']

print(x[0]) #1

print(x[2])   #[3, 'John', 4]

print(x[-1]) #Hi

print(x[2][2])  #4

print(x[0:1])   #[1] List 
 
print(2 in x) #True

print(3 in x)  #Flase

x[0] = 8

print(x[0])  # 8 instead of 1

L = [2,6,3,7,3,0]

print(sorted(L))

L.remove(2)
print(L)
L.remove(3)
L.sort()
print(L)
del(L[0])
print(L)
L.pop()
print(L)


s = "Hello ! there"
L = list(s)
print(L)
s.split('!')

print(s.split('!'))

#print(''.join(L))

print('_'.join(L))


print(L.insert(0,67))
print(L)

