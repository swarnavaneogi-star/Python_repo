while True:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    num3=int(input("Enter third number:"))

    if (num1>num2) and (num1>num3) and (num2>num3):
        print(f"{num1} is the largest number:")
        print(f"{num2} is the second largest number:")
    elif (num2>num1) and (num2>num3) and (num1>num3):
        print(f"{num2} is the largest number:")
        print(f"{num1} is the second largest number:")
    else:
        print(f"{num3} is the largest number:")
        if num1 > num2:
            print(f"{num1} is the second largest number:")
        else:
            print(f"{num2} is the second largest number:")

    cont =input("Do you want to enter another set of numbers  (yes/no):")
    if cont.lower()!="yes":
        print("Exiting the program ..")
        break
