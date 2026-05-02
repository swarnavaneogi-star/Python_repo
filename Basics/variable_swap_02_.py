# varible swap in python without third variable
a=int(input("Enter a number :"))#30
b=int(input("Enter another number: "))#20
print("The number before swapping are = \n",a,"and",b)
a= a+b
b= a-b
a= a-b
print("The number after swapping are =\n",a,"and",b)
