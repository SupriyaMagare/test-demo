
# Pattern 1
print("Pattern1")
for j in range(4):
    for i in range(4):
        print("*",end=" ")
    print()

# Pattern 2
print("Pattern2")
for i in range(4):
    for j in range(i+1):
      print("* ",end=" ")
    print()

#Pattern 3
print("Pattern3")
for i in range(4):
    for j in range(4-i):
        print(" * ",end=" ")
    print()
