class student:
    school= 'Magare'
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3

    def avg(self):
        return(self.m1+self.m2+self.m3)

    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is a student in class abc")


s1= student(35,25,45)
s2= student(88,45,55)

print(s1.avg())
print(student.getschool())

student.info()
