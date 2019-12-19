# Tupples= can not change values- iteration in tuples is faster than list

tup= (12,56,34,22,11)
print(tup)
print(tup[1])
#tup[2]=25  invalid assignment

# Set
#
S= {15,14,63,75,22}
print(S)

s= {22,90,43,22,88,11}
print(s)    # set dont consider duplicate values, indexing is not supported
s.add(16)
print(s)
s.discard(88)
print(s)

help()
