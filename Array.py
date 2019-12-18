
from array import *

vals = array('i',[5,9,8,4,2]) # array of integers
print(vals)
print(vals.buffer_info())   # buffer is size of array with address
vals.reverse()
print(vals)
print(vals[3])

for i in range(5):
    print(vals[i])

# for character array
print("Character array")
vals = array ('u',['a','e','i','o'])
newArr = array(vals.typecode, (a for a in vals)) # create newArr by copying existing vals array
for e in newArr:
    print(e)
