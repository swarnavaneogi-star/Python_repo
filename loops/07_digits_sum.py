while True:
    num=int(input("Enter a  number :"))
    d_sum=0
    d_count=0
    while num>0:
        digit=num%10
        d_sum+=digit
        d_count+=1
        num//=10

    print(f"The sum of digits is {d_sum}")
    print(f"The count of digits is {d_count}")
    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break