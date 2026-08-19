while True:
    num1=int(input("Enter a number :"))
    num2=int(input("Enter another number :"))
    if num1>num2: 
        smaller = num2
    else:
        smaller = num1
    gcd =1

    for i in range(1,smaller+1):
        if ((num1%i==0) and (num2%i==0)):
            gcd=i
    print(f"The Gcd of {num1} and {num2} is {gcd}")

    cont =input("Do you want to continue? (yes/no):")
    if cont.lower() != 'yes':
        break
