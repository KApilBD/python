grade= {'ana':'b', 'John':'a', 'katy':'a'}

print(grade['ana'])

grade['sylvan'] = 'c'


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

print(animals)

print(animals['c'])

print(len(animals))

#  print(animals['d']) # key not found

animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a']))

print('baboon' in animals)

print('donkey' in animals.values())

print('b' in animals)



print(animals.keys())

del animals['b']
print(len(animals))

print(animals.values())
