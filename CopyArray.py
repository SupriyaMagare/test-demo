from numpy import *

arr1= array([2,6,8,4,5])
arr2= arr1    # Alising array
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

print("Shallo Copy")

arr2 =arr1.view()
arr1[1]=7
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)

print("Deep Copy")
arr2=arr1.copy()
arr1[1]=5
print(arr1)
print(arr2)