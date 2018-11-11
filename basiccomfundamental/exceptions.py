# -*- coding: utf-8 -*-
"""

@author: Kapil
"""

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")

print("Correct input of an integer!")



data = []
file_name = input("Provide a name of a file of Data: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print("Can not open ", file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #Remove trailing \n
            data.append(addIt)
finally:
    fh.close()