while True:
    num=int(input("Enter a number :"))
    og=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    print("The reverse of the number is : ",rev)

    cont=input("Do you want to continue (yes/no) : ")
    if cont.lower()!="yes":
        break