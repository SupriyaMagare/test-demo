

def person(name,**data):
    print(name)
    for i,j in data.items():
         print(i,j)


person('Supriya', Age=28, City='Mumbai', mobile=992254)