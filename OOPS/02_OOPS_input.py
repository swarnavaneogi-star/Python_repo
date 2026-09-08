class Students:
    college = "Narula Institute of Technology" # class attribute

    def __init__(self): # Dunder method 
        self.name=""  # instance attribute 
        self.branch="" # instance attribute

    def input(self):
        self.name=input("Enter your name : ")
        self.branch=input("Enter your branch : ")

    def introduce(self):
        print(f"Name is :{self.name}")
        print((f"Branch is : {self.branch}"))
        print(f"College is : {Students.college}\n")  # accessing class attribute using class name
    
s1= Students()
s2= Students()
s3= Students()

s1.input()
s2.input()
s3.input()

s1.introduce()
s2.introduce()
s3.introduce()   