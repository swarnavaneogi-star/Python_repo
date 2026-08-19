while True:
    num=int(input("Enter a number to check factorial: "))
    if num<0:
        print("Factorial is not defined for negative numbers.")
    else :
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print(f"The factorial of {num} is : {fact}")

    cont=input("Do you want to continue (yes/no) : ")
    if cont.lower()!="yes":
         break