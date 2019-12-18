

f= open('MyData','r')
#print(f.readline(), end='#')
#print(f.readline(4))

f1= open('abc','a')
f1.write(" Laptop")

for data in f:
    f1.write(data)

f2= open('Image.jpg','rb')
f3= open('MyPic.jpg','wb')

for i in f2:
    f3.write(i)