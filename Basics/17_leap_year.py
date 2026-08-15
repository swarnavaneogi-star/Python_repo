while True:
    year = int(input("Enter a year: "))

    if (year % 4==0) or (year % 400==0) and (year % 100!=0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    cont = input("Do you want to enter another year? (yes/no): ")   
    if cont.lower() != "yes":
        print("Exiting the program. Goodbye!")
        break