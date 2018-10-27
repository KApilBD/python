
def gcdIter(a,b):
    if(a<b):
        i = a
        while i >0:
            if a%i==0 and b%i==0:
                return i
            i-=1
    else:
        i = b
        while i >0:
            if a%i==0 and b%i==0:
                return i       
            i-=1
            
            
print(gcdIter(17,12))


#alternate

def gcdIter2(a,b):
    
    testval = min(a,b)
    
    while a%testval !=0 or b%testval !=0:
        testval -= 1
    
    return testval

print(gcdIter2(9,12))


#Recursive

def gcdRecur(a, b):
    testval = min(a,b)
    return gcd(a,b,testval)

def gcd(a,b,testval):
    if a%testval ==0 and b%testval ==0:
        return testval
    else:
        return gcd(a,b,testval-1)

print(gcdRecur(6,12))

#Recusive using Euclidean's method

def gcdRecur(a,b):
    if b == 0:
        return a
    return gcdRecur(b, a%b)

print(gcdRecur(1071,462))

print(147%21)
