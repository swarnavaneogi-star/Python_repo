while True:
    num =int(input("Enter a number :"))
    fact_count=0
    sum_fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact_count+=1
            sum_fact+=i
            print(f"{i} is a factor of {num}")

    print(f"The number of factors are {fact_count} and the sum of factors is {sum_fact}")
    cont=input("Do you want to continue (yes/no):")
    if cont.lower()!='yes':
        break