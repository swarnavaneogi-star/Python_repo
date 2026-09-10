class Two_D_Vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def input_Two_D_Vector(self):
        self.i = int(input("Enter the coefficient of i for  2-d Vector  :"))
        self.j= int(input("Enter the coefficeint of j  for 2-d vector :"))

    def showmethod(self):
        print(f"The vector is {self.i}i + {self.j}j")

class Three_D_Vector(Two_D_Vector):
    def __init__(self ,i,j,k):
        super().__init__(i,j)
        self.k=k

    def input_Three_D_Vector(self):
        self.i = int(input("Enter the coefficient of i  for 3-d vector :"))
        self.j= int(input("Enter the coefficeint of j for 3-d vector :"))
        self.k = int(input("Enter the coefficient of k for 3-d vector :"))

    def showmethod(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a=Two_D_Vector(0,0)
a.input_Two_D_Vector()
a.showmethod()
b= Three_D_Vector(0,0,0)
b.input_Three_D_Vector()
b.showmethod()

