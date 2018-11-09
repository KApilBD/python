def how_many(aDict):
    '''
aDict: A dictionary, where all the values are lists.
return: int, how many individual values are in the dictionary.
'''
    result = 0
    for value in aDict.values():
        #Since all the values of aDict are lists, aDict.values() will be a list of lists
        result += len(value)
    return result

def how_many(aDict):
    '''
another way to solve the problem.
'''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['c'].append('cow')

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0 
    temp = None
    for key in aDict.keys():
        if biggest<= len(aDict[key]):
            temp = key
            biggest = len(aDict[key])
    return temp

print(biggest(animals))
            
