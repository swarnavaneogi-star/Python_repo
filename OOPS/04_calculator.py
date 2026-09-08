class calculator:
    def __init__(self):
        self.n1=0
        self.n2=0
        self.result=0
        self.result2=0

    def input(self):
        self.n1=int(input("Enter first number :"))
        self.n2=int(input("Enter second number :"))

    def add(self):
        self.result=self.n1+self.n2
        print(f"Addition of {self.n1} and {self.n2} is : {self.result}")

    def sub(self):
        self.result=self.n1-self.n2
        print(f"Subtraction of {self.n1} and {self.n2} is : {self.result}")

    def mul(self):
        self.result=self.n1*self.n2
        print(f"Multiplication of {self.n1} and {self.n2} is : {self.result}")

    def square(self):
        self.result=self.n1**2
        print(f"Square of {self.n1} is : {self.result}")
        self.result2=self.n2**2
        print(f"Square of {self.n2} is : {self.result2}")
        

    def cube(self):
        self.result=self.n1**3
        print(f"Cube of {self.n1} is : {self.result}")
        self.result2=self.n2**3
        print(f"Cube of {self.n2} is : {self.result2}")

    def divide(self):
        if(self.n2!=0):
            self.result=self.n1/self.n2
            print(f"Division of {self.n1} and {self.n2} is : {self.result}")
        else :
            print("Division not possible !!")
 
        
    def squareroot(self):
        self.result=self.n1**0.5
        print(f"Square root of {self.n1} is : {self.result}")
        self.result2=self.n2**0.5
        print(f"Square root of {self.n2} is : {self.result2}")

    def cuberoot(self):
        self.result=self.n1**(1/3)
        print(f"Cube root of {self.n1} is : {self.result}")
        self.result2=self.n2**(1/3)
        print(f"Cube root of {self.n2} is : {self.result2}")

choice=input("Enter your choice :\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square\n6.Cube\n7.Square root\n8.Cube root\n")

if choice == "1":
    obj=calculator()
    obj.input()
    obj.add()

elif choice == "2":
    obj=calculator()
    obj.input()
    obj.sub()

elif choice == "3":
    obj=calculator()
    obj.input()
    obj.mul()

elif choice == "4":
    obj=calculator()
    obj.input()
    obj.divide()

elif choice == "5":
    obj=calculator()
    obj.input()
    obj.square()

elif choice == "6":
    obj=calculator()
    obj.input()
    obj.cube()
    
elif choice == "7":
    obj=calculator()
    obj.input()
    obj.squareroot()

elif choice == "8":
    obj=calculator()
    obj.input()
    obj.cuberoot()

else :
     print ("Check your choice !!")