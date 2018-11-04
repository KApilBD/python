# -*- coding: utf-8 -*-

def isIn(char, aStr):
    
    if aStr == '':
        return False
    
    if len(aStr) == 1 :
        return aStr == char
    
    
    midIndex = len(aStr)//2
    mid = aStr[midIndex]
    
    if char == mid:
        return True
    elif char < mid:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])
            
print(isIn('k', 'abegkox'))

file = open('gdc.py', 'r')

for line in file:
    print(line)
file.close()