a=10
print( id(a))

def test():
     a=15
     x= globals()['a']
     print(id(x))
     print("In fun",a)
     globals()['a']=5

test()


print(a)