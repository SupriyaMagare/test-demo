


def greet():
    print(" Hello")
    print(" Good Morning")

greet()

def add(x,y):
    c=x+y
    print(c)

add(5,4)

def add_sub(a,b):
    r1 = a +b
    r2=  a- b
    return r1,r2
result1, result2 = add_sub(8,6)

print(result1, result2)
