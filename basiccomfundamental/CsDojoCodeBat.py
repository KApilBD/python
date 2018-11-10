# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:30:06 2018

@author: Kapil
"""

#def sleep_in(weekday, vacation):
#    if weekday == False or vacation == True:
#        return True
#    else:
#        return False
#Optimized
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    
def string_times(str, n):
    return str * n

print(string_times('hi', 4))

def first_last(lst):
    if lst[0] == 6 or lst[-1] == 6:
        return True
    else:
        False
        
a=[1,2,3,6]

print(first_last(a))

def double_char(str):
    temp =''
    for st in str:
        temp += st*2
    return temp

print(double_char('the'))


def count_evens(lst):
    temp = 0
    for i in lst:
        if i%2 == 0:
            temp +=1
    return temp

list = [1,2,3,4,5,6,7,8,16]
print(count_evens(list))