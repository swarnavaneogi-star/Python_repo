while True:
    largest_count=0 
    smallest_count=0
    largest=0
    smallest=0
    n=int(input("Enter the limit :"))
    for i in range(1,n+1):
        print("Enter number ",i,":")
        num=int(input())
        if i==1:
            largest=num
            smallest=num
        else:
            if num>largest:
                largest=num
                largest_count=1
            elif num==largest:
                largest_count+=1

            if num<smallest:
                smallest=num
                smallest_count=1
            elif num==smallest:
                smallest_count+=1
    print(f"The largest number is {largest} and it occurred {largest_count} times")
    print(f"The smallest number is {smallest} and it occurred {smallest_count} times")

    cont = input("Do you want to continue ? (yes/no) ") 
    if cont.lower() !="yes":
        break
