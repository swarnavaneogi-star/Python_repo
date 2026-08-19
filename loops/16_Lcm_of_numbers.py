
while True :
    num1=int(input("Enter a number:"))
    num2=int(input("Enter anothe number:"))
    
    if num1>num2:
        greater=num1
    else :
        greater=num2

    lcm =1
    
    for i in range(greater,num1*num2+1):
        if ((i%num1==0) and (i%num2==0)):
            lcm=i
            break
        
    print(f"The Lcm of {num1} and {num2} is {lcm}")


    cont=input("Do you want to continue (yes/no):")
    if cont.lower()!='yes':
        break


