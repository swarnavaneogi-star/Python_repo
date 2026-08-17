while True:
    n=int(input("Enter the limit :"))
    positive_count=0
    negative_count=0
    zero_count=0
    for i in range(1,n+1):
        print(f"Enter number {i}: ")
        num=int(input())
        if num>0:
            positive_count+=1
        elif num<0:
            negative_count+=1
        else:
            zero_count+=1
    print(f"The count of positive numbers is {positive_count}  ")
    print(f"The count of negative numbers is {negative_count}  ")
    print(f"The count of zero numbers is {zero_count}  ")

    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break