while True:
    num=int(input("Enter a  number :"))
    d_sum=0
    while num>0:
        digit=num%10
        d_sum+=digit
        num//=10

    print(f"The sum of digits is {d_sum}")
    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break