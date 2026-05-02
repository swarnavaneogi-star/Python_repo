#program to swap two numbers taken from the user 
a=int(input("Enter a number:"))
b=int(input("Enter another number :"))
print("The number before swapping are = \n",a,"and",b)
temp=a
a=b
b=temp
print("The number after swapping are =\n",a,"and",b)