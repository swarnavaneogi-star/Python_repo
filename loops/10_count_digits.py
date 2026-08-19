while True:
    num =int(input("Enter a number :"))
    dig_count=0
    while(num>0):
        dig_count+=1
        num=num//10
    print("The number of digits in the number is : ",dig_count)

    cont=input("Do you want to continue (yes/no) : ")
    if cont.lower()!="yes":
        break