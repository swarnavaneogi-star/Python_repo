class Students:
    college = "Narula Institute of Technology" # class attribute

    def __init__(self,name,branch):
        self.name=name # instance attribute 
        self.branch=branch  # instance attribute

    def introduce(self):
        print(f"Name is :{self.name}")
        print((f"Branch is : {self.branch}"))
        print(f"College is : {Students.college}\n")  # accessing class attribute using class name

s1= Students("Swarnava Neogi","AIML")
s2= Students("Sayan Ghosh","CSE")
s3= Students("Aniket Roy","DSE") 

s1.introduce()
s2.introduce()
s3.introduce()   