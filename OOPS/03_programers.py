class Programs:
    office = "Microsoft" # class attribute

    def __init__(self): 
        self.name=""
        self.language=""
        self.salary=""
        self.age=""

    def input(self):
        self.name =input("Enter employee's name :")
        self.language =input("Enter employee's working language :")
        self.salary =int(input("Enter employee's salary :"))
        self.age =int(input("Enter employee's age :"))

    def introduce(self):
        print(f"Name is :{self.name}")
        print(f"Language is : {self.language}")
        print(f"Salary is : {self.salary}")
        print(f"Age is : {self.age}")
        print(f"Office is : {Programs.office}\n")  # accessing class attribute using class

e1=Programs()
e2=Programs()



e1.input()
e1.introduce()

e2.input()
e2.introduce()

