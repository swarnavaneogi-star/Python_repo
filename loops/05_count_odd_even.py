while True:
    n=int(input("Enter the limit :"))
    odd_count=0
    even_count=0
    for i in range(1,n+1):
        num=int(input(f"Enter number {i}: "))
        if num%2==0:
            even_count+=1
        else:
            odd_count+=1
    print(f"The count of odd numbers is {odd_count}  ")
    print(f"The count of even numbers is {even_count}  ")

    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break
    