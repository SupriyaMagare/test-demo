# Example1
if ('Python' in ['Java','C#','Python']):
    print("Python is present in the list")
if('C#' in ['Java','C#','Python']):
    print("C# is present in the list")
if('Java' in ['Java','C#','Python']):
    print("Java is present in the list")

# Example 2 Nested if
print("Example2")
num=-7
if (num!=0):
    if(num>0):
            print("Number is Positive")
    else:
            print("Number is Negative")
else:
    print("number is zero")


#Elif Ladder
my_marks= int( input("Enter your Marks"))
if(my_marks < 35):
    print("Sorry you are failed in the exam")
elif(my_marks<60):
    print("Passed in the second class")
elif(my_marks>60 and my_marks< 85):
    print("Passed in the first class")
else:
    print('Passed in the distinction')