print(map(abs, [1,-2,3,-4]))

l=list(map(abs, [1,-2,3,-4]))
print(l)  #>>[1,2,3,4]


def addOne(num):
    return num+1

li=list(map(addOne, l))
print(li)  #>>[2,3,4,5]

lis = map(addOne, li)
print(lis.__next__())  #>>3
print(lis.__next__())  #>>4
print(lis.__next__())  #>>5
print(lis.__next__())  #>>6


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

def mulByFiv(x):
    return 5*x

applyToEach(testList, mulByFiv)
print(testList)
print(testList)

nL = [1, 4, 8, 9]

print(nL)
def applytooEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i], i)

def myFun(x, i):
        if i%2 == 0:
            x = x+1
            return x
        else:
            x = x -10
            return x
            
applytooEach(nL, myFun)

print(nL)



def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
        print(str(result)+" "+str(L[i]))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

listt=list(applyEachTo([inc, square, halve, abs], 3.0))
print(listt)




