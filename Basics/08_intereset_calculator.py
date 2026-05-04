#python program to calculate the interest 
while True :
    print("Enter the principal amount:")
    p=float(input())
    og =p
    print("Enter the rate of interest:")
    r=float(input())
    print("Enter the time in years :")
    t=float(input())

    if p<=0 or t<=0 or r<=0:
        print("Please enter valid inputs to calculate the interest:")
        continue 

    si=(p*r*t)/100 # simple interest formula
    ci=p*(1+(r/100))**t - p # compound interest formula
    total = si+p # total amount after adding simple interest to the principal
    cl_total = ci+p # total amount after adding compound interest to the principal
    print(f"\nThe principal amount is : ${og}")
    print(f"The rate of interest is : {r}%")
    print(f"The time period is : {t} years")
    print("\n")
    print(f"\nThe simple interest is : ${si}")
    print(f"The compound interest is : ${ci}")
    print("\n")
    print(f"The total amount after adding simple interest is : ${total}")
    print(f"The total amount after adding compound interest is : ${cl_total}")

    cont = input("Do you want to enter for another amount? (yes/no): ")
    if cont.lower() != 'yes':
        print("Exiting the program. Goodbye!")
        print("Thank you for using the Interest Calculator.")
        break