#Euclidean Algorithm for finding GCD/HCF
while True :
    num1=int(input("Enter a number:"))
    num2=int(input("Enter anothe number:"))
    
    while num2!=0:
        remainder=num1%num2
        num1=num2
        num2=remainder

    print("the gcd of the numbers is :",num1)

    cont=input("Do you want to continue (yes/no):")
    if cont.lower()!='yes':
        break


