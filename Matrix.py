from numpy import *

m = matrix('1,2,3;4,5,6;3,2,2;1,1,1')

print(m)
print(m.min())
print(m.max())

# Addition of Matrix

m1= matrix ('1,2,3;6,5,1;3,2,1')
m2= matrix('1,2,6;3,4,1;2,7,5')
#print(m1)
#print(m2)

m3= m1*m2
print(m3)