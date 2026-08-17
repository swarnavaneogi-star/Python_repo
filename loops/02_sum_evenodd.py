while True:
    n=int(input("Enter the limit :"))
    even_sum=0
    odd_sum=0
    for i in range (1,n+1):
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    print(f"The sum of first {n} odd numbers is {odd_sum}  ")
    print(f"The sum of first {n} even numbers is {even_sum}  ")

    cont = input("Do you want to continue ? (yes/no) ")
    if cont.lower() !="yes":
        break

    