#A python program to build a simple calculator , which can perform operations 

a = int(float(input("Enter a number :")))
b = int(float(input("Enter another number :")))
print("Select an operations to you want to perform ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("enter your choice"))
if choice==1:
    print("The sum of ",a,"and",b,"is =",a+b)
elif choice==2:
    print("The difference of ",a,"and",b,"is =",a-b)
elif choice==3:
    print("The product of ",a,"and",b,"is =",a*b)
elif choice==4:
    if b!=0:
        print("The quotient of ",a,"and",b,"is =",a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")
    