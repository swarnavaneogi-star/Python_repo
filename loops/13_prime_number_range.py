while True:
    a=int(input("Enter the starting number of the range :"))
    b=int(input("Enter the ending number of the range :"))
    print(f"The prime numbers between {a} and {b} are : ")
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num,end=" ")
    print()
    cont=input("Do you want to continue (yes/no) : ")
    if cont.lower()!="yes":
        break