while True:
    n = int(input("enter a number :"))

    for i in range(1,15):
        if n%i==0:
            print(f"{n} is divisible by {i}")


    cont = input("Do you want to enter another number? (yes/no): ")
    if cont.lower() != "yes":
        print("Exiting the program. Goodbye!")
        break