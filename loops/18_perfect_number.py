while True:
    num =int(input("Enter a number :"))
    sum_fact=0
    temp=num
    for i in range(1,temp-1):
        if temp%i==0:
            sum_fact+=i

    if (num==sum_fact):
        print(f"{num} is a Perfect number")
    else:
        print(f"{num} is not a Perfect number")

    cont=input("Do you want to continue (yes/no):")
    if cont.lower()!='yes':
        break
