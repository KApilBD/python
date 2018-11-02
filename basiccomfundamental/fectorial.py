

#def fecto(n):
#    if(n==1):
#        return 1
#    else:
#        return n*fecto(n-1)
#    
#    
#print(fecto(5))

def iterPower(base, exp):
    result = 1
    while exp>0:
        result *=base
        exp -= 1
    return result

print(iterPower(2.1, 7))


def iterPower(base, exp):
    if(exp == 0):
        return 1
    else:
        return base*iterPower(base, exp-1)
    
print(iterPower(2.1, 7))
