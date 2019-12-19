from array import *

arr= array('i',[])
n= int(input("Enter the length of the Array"))

for i in range(n):
    x= int(input("Enter the next value"))
    arr.append(x)
print(arr)

val= int(input("Enter the value you want to search" ))
k=0;
for e in arr:                   #Code for Manually searching element of arrray
    if e== val:
        print(k)
        break
    else:
        k+=1

print(arr.index(val))                 # accessjing element of array by function