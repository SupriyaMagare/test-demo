from numpy import *

arr= array([1,2,3,4,5.0])   # implicit conversion of array value in the type

print(arr.dtype)
print(arr)

arr= array([1,2,3,4,5], float)   # specifying type of array
print(arr)
# linspace
print("Linspace")
arr = linspace(0,15,10)   # 10 is number of parts divided
print(arr)

print("A range")
arr= arange(1,15,3)     # range
print(arr)

print("Logspace")
arr= logspace(1,40,5)
print(arr)