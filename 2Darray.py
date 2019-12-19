from numpy import *

arr1= array([
                [1,2,3],
                [4,5,6]
])

print(arr1.ndim) # dimension of array
print(arr1.shape) # number of rows and columns
print(arr1. size)  # number of elements in the array
arr2= arr1.flatten()
print(arr2)
arr3 = array([
                [1,2,4,2,5,6],
                [7,2,3,4,3,0]
])
arr4= arr3.reshape(2,2,3)

print(arr4)

