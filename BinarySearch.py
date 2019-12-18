
pos= -1

def search(list, n):
    l=0
    u=len(list)-1
    while(1<u):
        mid= (l+u)//2     # integer division
        if list[mid]==n:
            globals()['pos']= mid
            return True
        else:
            if list[mid]<n:
                l= mid+1
            else:
                u= mid-1

list= [12,34,45,56,88,33,98,35,100,345,23,]
n= 34

if search(list,n):
    print(" Found at ", pos+1)
else:
    print("Not Found")