while True:
    num =int(input("Enter a the limit for the fibonacci series:"))
    a=0
    b=1
    print("The fibonacci series is : ")
    for i in range(num):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    print()
    cont=input("Do you want to continue (yes/no) : ")
    if cont.lower()!="yes":
       break
