while True:    
    n=int(input("Enter the limit :"))
    sum=0
    for i in range(1,n+1):
        sum =sum+i
    print(f"The sum of first {n} natural numbers is {sum}")
    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break
  