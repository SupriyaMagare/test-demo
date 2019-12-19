def search(list,n):

    for i in range(6):
        if list[i]==n:
            print("Found")
        else:
            print("Not found")


list = [2,5,6,9,2,1]
n=9

if search(list,n):
    True
else:
    False