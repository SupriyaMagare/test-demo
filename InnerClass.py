class student:

    def __init__(self, name,rollno):
        self.name = name
        self.rollno= rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand= 'Hp'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu, self.ram)

s1 = student('Supriya',1)
s2 = student('Siddhi',5)

s1.show()

