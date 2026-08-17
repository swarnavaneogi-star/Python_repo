import math
while True:
    n= int(input("Enter the limit :"))
    for i in range(1,n+1):
        print(f"The square of {i} is {math.pow(i,2)}")

    cont =input("Do you want to continue ? (yes/no) ")
    if cont.lower!="yes":
        break
